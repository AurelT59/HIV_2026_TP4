#!/usr/bin/env python3
"""Mesure la couverture (lignes + branches) des tests Q1 avec pytest."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "outputs" / "Q1"
TARGETS_DIR = ROOT / "poly_llm" / "to_test"


def discover_tests(prefix: str) -> list[Path]:
    return sorted(TESTS_DIR.glob(f"test_{prefix}_*.py"))


def target_from_test(test_path: Path) -> Path:
    name = test_path.stem
    suffix = name.replace("test_zero_shot_", "").replace("test_few_shot_", "")
    return TARGETS_DIR / f"{suffix}.py"


def summarize_pytest_failure(output: str) -> str:
    failed_lines = [line.strip() for line in output.splitlines() if line.strip().startswith("FAILED ")]
    if failed_lines:
        return " | ".join(failed_lines)

    match = re.search(r"(\d+\s+failed[^\n]*)", output)
    if match:
        return match.group(1).strip()

    return "pytest a échoué (voir logs détaillés)."


def run_coverage_for_test(test_path: Path) -> tuple[float | None, float | None, str | None]:
    target = target_from_test(test_path)
    if not target.exists():
        return None, None, f"Fichier cible introuvable: {target.relative_to(ROOT)}"

    with tempfile.TemporaryDirectory() as tmp:
        report_json = Path(tmp) / "coverage.json"

        run_cmd = [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "--branch",
            "-m",
            "pytest",
            str(test_path.relative_to(ROOT)),
            "-q",
        ]
        run_result = subprocess.run(run_cmd, cwd=ROOT, capture_output=True, text=True)
        pytest_error: str | None = None
        if run_result.returncode != 0:
            err = (run_result.stdout + "\n" + run_result.stderr).strip()
            pytest_error = summarize_pytest_failure(err)

        json_cmd = [
            sys.executable,
            "-m",
            "coverage",
            "json",
            "-o",
            str(report_json),
        ]
        json_result = subprocess.run(json_cmd, cwd=ROOT, capture_output=True, text=True)
        if json_result.returncode != 0:
            err = (json_result.stdout + "\n" + json_result.stderr).strip()
            if pytest_error:
                return None, None, f"{pytest_error} | coverage json a échoué: {err}"
            return None, None, f"coverage json a échoué: {err}"

        data = json.loads(report_json.read_text(encoding="utf-8"))
        wanted = target.resolve().as_posix()

        for file_path, metrics in data.get("files", {}).items():
            if Path(file_path).resolve().as_posix() == wanted:
                summary = metrics["summary"]
                covered_lines = summary.get("covered_lines", 0)
                total_lines = summary.get("num_statements", 0)
                line = 100.0 * covered_lines / total_lines if total_lines else 100.0

                covered_branches = summary.get("covered_branches", 0)
                total_branches = summary.get("num_branches", 0)
                branch = 100.0 * covered_branches / total_branches if total_branches else 100.0

                return line, branch, pytest_error

        if pytest_error:
            return None, None, f"{pytest_error} | Aucune donnée pour {target.relative_to(ROOT)}"
        return None, None, f"Aucune donnée pour {target.relative_to(ROOT)}"


def print_table(title: str, tests: list[Path]) -> None:
    print(f"\n{title}")
    print("| Test | Couverture lignes (%) | Couverture branches (%) |")
    print("|---|---:|---:|")
    errors: list[tuple[str, str]] = []

    for test in tests:
        line, branch, error = run_coverage_for_test(test)
        display_name = test.name
        if line is None or branch is None:
            print(f"| {display_name} | erreur | erreur |")
            if error:
                errors.append((display_name, error))
            continue

        print(f"| {display_name} | {line:.2f} | {branch:.2f} |")
        if error:
            errors.append((display_name, f"tests en échec (couverture calculée): {error}"))

    if errors:
        print("\nDétails des erreurs :")
        for test_name, message in errors:
            print(f"- {test_name}: {message}")


def main() -> int:
    zero_shot = discover_tests("zero_shot")
    few_shot = discover_tests("few_shot")

    if len(zero_shot) != 5 or len(few_shot) != 5:
        print(
            "Attention: ce script est prévu pour 5 tests zero shot et 5 tests few shot, "
            f"mais a trouvé {len(zero_shot)} et {len(few_shot)}.",
            file=sys.stderr,
        )

    print_table("Tableau 1 - Zero shot", zero_shot)
    print_table("Tableau 2 - Few shot", few_shot)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
