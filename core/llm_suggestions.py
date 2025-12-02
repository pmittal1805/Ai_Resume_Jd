# core/llm_suggestions.py
from typing import List

# If you want to use OpenAI later, you can uncomment and configure:
# import openai
# openai.api_key = "YOUR_API_KEY"

def suggest_improvements_stub(resume_text: str, jd_text: str, matched_skills: List[str], missing_skills: List[str]) -> str:
    """
    Placeholder function.
    Later you can replace with real LLM call (OpenAI/HF).
    """
    suggestion = [
        "This is a basic suggestion (no LLM yet):",
        f"- You match these important skills: {', '.join(matched_skills) if matched_skills else 'None'}",
        f"- You are missing these key skills from the JD: {', '.join(missing_skills) if missing_skills else 'None'}",
        "",
        "You should:",
        "- Add 1–2 bullets for projects that use the missing skills (if you know them).",
        "- Make sure your project descriptions include metrics (accuracy, F1, RMSE, etc.).",
    ]
    return "\n".join(suggestion)
