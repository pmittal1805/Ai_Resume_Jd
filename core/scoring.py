# core/scoring.py
from typing import List, Dict
import numpy as np
from .embeddings import embed_texts

def compute_skill_match(jd_skills: List[str], resume_skills: List[str]) -> Dict:
    jd_set = set(jd_skills)
    res_set = set(resume_skills)

    matched = jd_set & res_set
    missing = jd_set - res_set

    if len(jd_set) == 0:
        skill_match_pct = 0.0
    else:
        skill_match_pct = len(matched) / len(jd_set) * 100.0

    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "skill_match_pct": round(skill_match_pct, 1),
    }


def compute_text_similarity(jd_text: str, resume_text: str) -> float:
    """
    Use sentence embeddings to compute semantic similarity between JD and resume.
    """
    if not jd_text.strip() or not resume_text.strip():
        return 0.0

    embeddings = embed_texts([jd_text, resume_text])
    jd_emb, res_emb = embeddings[0], embeddings[1]

    sim = float(np.dot(jd_emb, res_emb))  # because we normalized, dot = cosine
    # convert cosine (-1..1) to 0..100
    sim_pct = (sim + 1) / 2 * 100
    return round(sim_pct, 1)


def compute_overall_score(skill_match_pct: float, text_sim_pct: float) -> float:
    """
    Simple combined score.
    You can tune weights later.
    Example: 60% weight skills, 40% weight semantic similarity.
    """
    score = 0.6 * skill_match_pct + 0.4 * text_sim_pct
    return round(score, 1)
