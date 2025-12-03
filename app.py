# app.py
import streamlit as st

from core.parse_resume import extract_resume_text
from core.parse_jd import clean_jd_text
from core.skills_extract import load_skill_dictionary, extract_skills
from core.scoring import compute_skill_match, compute_text_similarity, compute_overall_score
from core.llm_suggestions import suggest_improvements_stub


def main():
    st.set_page_config(page_title="AI Resume & JD Analyzer", layout="wide")
    st.title("🧠 AI Resume & Job Description Analyzer")

    st.write("Upload your resume and paste a job description to analyze skill match and fit.")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

    with col2:
        jd_text_raw = st.text_area(
            "Paste Job Description here",
            height=260,
            placeholder="Paste the full JD here..."
        )

    if st.button("Analyze"):

        if not resume_file:
            st.error("Please upload a resume file.")
            return
        if not jd_text_raw.strip():
            st.error("Please paste a job description.")
            return

        with st.spinner("Extracting resume text..."):
            resume_text = extract_resume_text(resume_file)

        with st.spinner("Cleaning job description..."):
            jd_text = clean_jd_text(jd_text_raw)

        # Load skill dictionary
        skill_dict = load_skill_dictionary("data/skill_dictionary.txt")

        # Extract skills (FIXED: use extract_skills, not extract_skills_from_text)
        with st.spinner("Extracting skills from resume and JD..."):
            resume_skills = extract_skills(resume_text, skill_dict)
            jd_skills = extract_skills(jd_text, skill_dict)

            # Debug lines (optional; you can remove later)
            st.write("DEBUG JD skills:", jd_skills)
            st.write("DEBUG Resume skills:", resume_skills)

        # Compute scores
        with st.spinner("Computing match scores..."):
            skill_info = compute_skill_match(jd_skills, resume_skills)
            text_sim_pct = compute_text_similarity(jd_text, resume_text)
            overall_score = compute_overall_score(
                skill_info["skill_match_pct"],
                text_sim_pct
            )

        # Display results
        st.subheader("📊 Match Overview")
        st.metric("Overall Match Score", f"{overall_score} / 100")
        st.metric("Skill Match", f"{skill_info['skill_match_pct']} %")
        st.metric("Semantic Similarity (JD vs Resume)", f"{text_sim_pct} %")

        col_a, col_b = st.columns(2)

        with col_a:
            st.subheader("✅ Matched Skills")
            if skill_info["matched_skills"]:
                st.write(", ".join(skill_info["matched_skills"]))
            else:
                st.write("No matching skills found from dictionary.")

        with col_b:
            st.subheader("⚠️ Missing Skills (from JD)")
            if skill_info["missing_skills"]:
                st.write(", ".join(skill_info["missing_skills"]))
            else:
                st.write("No missing skills from dictionary (or JD had none).")

        # Suggestions (stub or LLM later)
        st.subheader("🧩 Suggestions / Next Steps")
        suggestions = suggest_improvements_stub(
            resume_text,
            jd_text,
            skill_info["matched_skills"],
            skill_info["missing_skills"],
        )
        st.code(suggestions, language="markdown")

        # Optional: show raw sections for debug
        with st.expander("🔍 View Raw Resume & JD Text"):
            st.text_area("Resume Text (Extracted)", resume_text, height=200)
            st.text_area("Job Description (Cleaned)", jd_text, height=200)


if __name__ == "__main__":
    main()
