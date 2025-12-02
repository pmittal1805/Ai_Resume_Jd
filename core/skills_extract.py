# core/skills_extract.py
import re
from typing import List, Set

def load_skill_dictionary(path: str = "data/skill_dictionary.txt") -> Set[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            skills = [line.strip().lower() for line in f if line.strip()]
        return set(skills)
    except FileNotFoundError:
        # fallback default list
        default_skills = [
            "python", "pandas", "numpy", "matplotlib", "seaborn",
            "scikit-learn", "sklearn", "tensorflow", "pytorch",
            "nlp", "natural language processing", "hugging face", "transformers",
            "llm", "deep learning", "machine learning", "sql",
            "flask", "fastapi", "streamlit", "git", "docker",
            "azure", "aws", "gcp", "linux"
        ]
        return set(default_skills)


def normalize_text(text: str) -> str:
    return re.sub(r"[^a-z0-9+.# ]+", " ", text.lower())


def extract_skills_from_text(text: str, skill_dict: Set[str]) -> List[str]:
    """
    Very simple skill extraction:
    - normalize text
    - match known skill phrases
    """
    norm = normalize_text(text)
    found = set()
    for skill in skill_dict:
        if skill in norm:
            found.add(skill)
    return sorted(found)
