from scripts.llm_pipeline import run_question, print_markdown


if __name__ == "__main__":
    results = run_question(question="Q3", model_name="codellama/CodeLlama-7b-Instruct-hf", provider="huggingface", max_new_tokens=220)
    print_markdown(results, "Q3")
    print("\nRapport JSON: outputs/Q3/report_q3.json")
