from __future__ import annotations

import argparse
import ast
import importlib
import inspect
import json
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator

ROOT = Path(__file__).resolve().parents[1]

PUTS = [
    "closest_integer",
    "file_name_check",
    "find_closest_elements",
    "numerical_letter_grade",
    "separate_paren_groups",
]


@dataclass
class PutContext:
    name: str
    func: Callable
    base_test: Callable
    source_path: Path


def load_put_context(name: str) -> PutContext:
    module = importlib.import_module(f"poly_llm.to_test.{name}")
    func = getattr(module, name)
    test_fn = getattr(module, f"test_{name}")
    return PutContext(name=name, func=func, base_test=test_fn, source_path=Path(module.__file__))


def extract_assertions_from_base_test(ctx: PutContext) -> list[str]:
    source = inspect.getsource(ctx.base_test)
    tree = ast.parse(textwrap.dedent(source))
    assertions: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            assertions.append(f"assert {ast.unparse(node.test)}")
    return assertions


def measure_initial_coverage_with_abstract_executor(ctx: PutContext) -> dict:
    executor = AbstractExecutor(ctx.base_test)
    data = executor._execute_input()
    coverage = data.get("coverage", {})
    lines = coverage.get("covered_lines", 0)
    total_lines = coverage.get("num_statements", 0)
    branches = coverage.get("covered_branches", 0)
    total_branches = coverage.get("num_branches", 0)
    return {
        "line_pct": (100.0 * lines / total_lines) if total_lines else 0.0,
        "branch_pct": (100.0 * branches / total_branches) if total_branches else 0.0,
        "raw": coverage,
    }


def build_few_shot_examples(assertions: list[str], variant: int) -> list[str]:
    if not assertions:
        return []
    if variant == 1:
        chosen = assertions[:1]
    elif variant == 2:
        chosen = assertions[:2]
    else:
        chosen = assertions
    body = "\n    ".join(chosen)
    return [f"def test_example():\n    {body}\n"]


def generate_prompt(ctx: PutContext, mode: str, few_variant: int | None = None) -> str:
    pg = PromptGenerator(ctx.func)
    if mode == "zero_shot":
        return pg.generate_prompt()
    examples = build_few_shot_examples(extract_assertions_from_base_test(ctx), few_variant or 1)
    return pg.generate_prompt(few_shot_examples=examples)


def ensure_dirs(question: str) -> tuple[Path, Path]:
    prompts_dir = ROOT / "prompts" / question
    outputs_dir = ROOT / "outputs" / question
    prompts_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    return prompts_dir, outputs_dir


def parse_asserts_from_text(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if ln.strip().startswith("assert ")]


def generate_with_hf_local(prompt: str, model_name: str, max_new_tokens: int) -> str:
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.2)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def generate_test_file_content(ctx: PutContext, generated_text: str, include_base_assertions: bool) -> str:
    asserts = parse_asserts_from_text(generated_text)
    if not asserts:
        asserts = [f"assert {ctx.name} is not None"]

    base_asserts = extract_assertions_from_base_test(ctx) if include_base_assertions else []
    all_asserts = base_asserts + asserts
    indented = "\n    ".join(all_asserts)

    return (
        f"from poly_llm.to_test.{ctx.name} import {ctx.name}\n\n"
        f"def test_llm_{ctx.name}():\n"
        f"    {indented}\n"
    )


def measure_coverage_for_test_file(ctx: PutContext, test_file: Path) -> tuple[float, float, str | None]:
    with tempfile.TemporaryDirectory() as tmp:
        report_json = Path(tmp) / "cov.json"
        run_cmd = [sys.executable, "-m", "coverage", "run", "--branch", "-m", "pytest", str(test_file.relative_to(ROOT)), "-q"]
        run = subprocess.run(run_cmd, cwd=ROOT, text=True, capture_output=True)
        failure = None
        if run.returncode != 0:
            summary = [l.strip() for l in (run.stdout + "\n" + run.stderr).splitlines() if l.strip().startswith("FAILED ")]
            failure = " | ".join(summary) if summary else "pytest failed"

        json_cmd = [sys.executable, "-m", "coverage", "json", "-o", str(report_json)]
        jrun = subprocess.run(json_cmd, cwd=ROOT, text=True, capture_output=True)
        if jrun.returncode != 0:
            return 0.0, 0.0, f"coverage json failed: {jrun.stderr.strip()}"

        data = json.loads(report_json.read_text(encoding="utf-8"))
        wanted = ctx.source_path.resolve().as_posix()
        for fpath, metrics in data.get("files", {}).items():
            if Path(fpath).resolve().as_posix() == wanted:
                s = metrics["summary"]
                lp = (100.0 * s.get("covered_lines", 0) / s.get("num_statements", 1)) if s.get("num_statements", 0) else 0.0
                bp = (100.0 * s.get("covered_branches", 0) / s.get("num_branches", 1)) if s.get("num_branches", 0) else 0.0
                return lp, bp, failure
    return 0.0, 0.0, "no coverage data"


def run_question(question: str, model_name: str, provider: str, max_new_tokens: int) -> dict:
    prompts_dir, outputs_dir = ensure_dirs(question)
    results: dict[str, dict] = {}

    for put_name in PUTS:
        ctx = load_put_context(put_name)
        baseline = measure_initial_coverage_with_abstract_executor(ctx)

        modes = [("zero_shot", 0), ("few_shot", 1)]
        if question == "Q2":
            modes.extend([("few_shot_v2", 2), ("few_shot_v3", 3)])

        put_results = {"baseline": baseline, "experiments": []}
        for mode, variant in modes:
            prompt_mode = "zero_shot" if mode == "zero_shot" else "few_shot"
            prompt = generate_prompt(ctx, prompt_mode, variant)
            prompt_file = prompts_dir / f"prompt_{put_name}_{mode}.txt"
            prompt_file.write_text(prompt, encoding="utf-8")

            if provider == "stub":
                generated_text = "\n".join(extract_assertions_from_base_test(ctx))
            else:
                generated_text = generate_with_hf_local(prompt, model_name, max_new_tokens)

            test_content = generate_test_file_content(ctx, generated_text, include_base_assertions=True)
            test_file = outputs_dir / f"test_{mode}_{put_name}.py"
            test_file.write_text(test_content, encoding="utf-8")

            line_pct, branch_pct, failure = measure_coverage_for_test_file(ctx, test_file)
            put_results["experiments"].append(
                {
                    "mode": mode,
                    "prompt_file": str(prompt_file.relative_to(ROOT)),
                    "test_file": str(test_file.relative_to(ROOT)),
                    "line_pct": line_pct,
                    "branch_pct": branch_pct,
                    "delta_line": line_pct - baseline["line_pct"],
                    "delta_branch": branch_pct - baseline["branch_pct"],
                    "failure": failure,
                }
            )

        results[put_name] = put_results

    summary_file = outputs_dir / f"report_{question.lower()}.json"
    summary_file.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return results


def print_markdown(results: dict, question: str) -> None:
    print(f"\n# Résultats {question}")
    for put_name, payload in results.items():
        base = payload["baseline"]
        print(f"\n## {put_name}")
        print("| Expérience | Ligne % | Branche % | Δ ligne | Δ branche | Statut |")
        print("|---|---:|---:|---:|---:|---|")
        print(f"| baseline assertions | {base['line_pct']:.2f} | {base['branch_pct']:.2f} | 0.00 | 0.00 | ok |")
        for exp in payload["experiments"]:
            status = "ok" if not exp["failure"] else "tests en échec"
            print(
                f"| {exp['mode']} | {exp['line_pct']:.2f} | {exp['branch_pct']:.2f} | "
                f"{exp['delta_line']:.2f} | {exp['delta_branch']:.2f} | {status} |"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", choices=["Q2", "Q3"], required=True)
    parser.add_argument("--provider", choices=["hf-local", "stub"], default="stub")
    parser.add_argument("--model", default="Salesforce/codegen-350M-mono")
    parser.add_argument("--max-new-tokens", type=int, default=220)
    args = parser.parse_args()

    results = run_question(
        question=args.question,
        model_name=args.model,
        provider=args.provider,
        max_new_tokens=args.max_new_tokens,
    )
    print_markdown(results, args.question)
    print(f"\nRapport JSON: outputs/{args.question}/report_{args.question.lower()}.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
