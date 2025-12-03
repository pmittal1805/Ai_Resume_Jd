import re

def load_skill_dictionary(path: str) -> set[str]:
    skills = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            skill = line.strip().lower()
            if skill:
                skills.add(skill)
    return skills


def extract_skills(text: str, skill_dict: set[str]) -> set[str]:
    """
    Simple matching: lowercase text and check if each skill appears.
    Works for one-word and multi-word skills.
    """
    text_lower = text.lower()
    found = set()

    for skill in skill_dict:
        if " " in skill:
            # multi-word skill (e.g., "machine learning")
            if skill in text_lower:
                found.add(skill)
        else:
            # single word skill (e.g., "python")
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, text_lower):
                found.add(skill)

    return found
