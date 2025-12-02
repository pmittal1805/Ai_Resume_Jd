# core/parse_jd.py
import re

def clean_jd_text(raw_jd: str) -> str:
    """Basic cleaning: remove extra spaces, bullets, etc."""
    text = raw_jd.replace("\r", "\n")
    text = re.sub(r"\n+", "\n", text)
    text = text.strip()
    return text
