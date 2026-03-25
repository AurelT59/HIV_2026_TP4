from scripts.llm_pipeline import run_question, print_markdown


if __name__ == "__main__":
    results = run_question(question="Q2", model_name="microsoft/phi-2", provider="huggingface", max_new_tokens=220)
    print_markdown(results, "Q2")
    print("\nRapport JSON: outputs/Q2/report_q2.json")
