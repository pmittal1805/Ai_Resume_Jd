# AI Resume & Job Description Analyzer

An **end-to-end NLP-based application** that analyzes a candidate’s resume against a given Job Description (JD) and provides **skill matching, similarity score, and improvement suggestions**. This project is designed for **AI/ML & NLP internship interviews** and demonstrates real-world usage of **NLP, embeddings, and semantic similarity**.

---

## 🔍 Project Overview

Recruiters manually screening resumes is time-consuming and subjective. This project automates the process by:

* Extracting text from resumes (PDF / DOCX)
* Processing Job Descriptions
* Comparing resume content with JD using **semantic similarity**
* Highlighting missing skills and suggestions for improvement

The system does **not rely on simple keyword matching only**; it uses **sentence embeddings** for deeper semantic understanding.

---

## 🚀 Features

* Upload Resume (PDF / DOCX)
* Paste or upload Job Description
* Skill extraction & comparison
* Resume–JD similarity score
* Missing skill detection
* Improvement suggestions
* Clean Streamlit-based UI

---

## 🧠 Tech Stack

### Languages & Frameworks

* **Python 3.9+**
* **Streamlit** – Web UI

### NLP & ML

* **Sentence-Transformers** (Hugging Face)
* **Transformer-based embeddings**
* **Cosine Similarity**
* **Scikit-learn**

### File Processing

* **PyMuPDF (fitz)** – PDF parsing
* **python-docx** – DOCX parsing

---

## 📂 Project Structure

```
Ai_Resume_Jd/
│
├── app.py                     # Main Streamlit application
├── core/
│   ├── parse_resume.py        # Resume text extraction logic
│   ├── similarity.py          # Embedding & similarity calculations
│   ├── skill_matcher.py       # Skill matching logic
│
├── data/
│   └── skill_dictionary.txt   # Predefined skill set
│
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── assets/                    # Optional UI assets
```

---

## ⚙️ Workflow Explanation

1. **Resume Upload**

   * PDF/DOCX resume is uploaded
   * Text extracted using PyMuPDF / python-docx

2. **Job Description Input**

   * JD is entered manually or uploaded

3. **Text Preprocessing**

   * Lowercasing
   * Noise removal
   * Token normalization

4. **Embedding Generation**

   * Resume & JD converted into embeddings using `sentence-transformers`

5. **Similarity Calculation**

   * Cosine similarity applied to measure match percentage

6. **Skill Matching**

   * Resume & JD compared against `skill_dictionary.txt`
   * Missing and matched skills identified

7. **Suggestions Output**

   * Suggestions generated based on missing skills

---

## 📊 Output Explanation

* **Similarity Score (%)** – How well resume matches JD
* **Matched Skills** – Skills found in both resume & JD
* **Missing Skills** – Important JD skills absent in resume
* **Suggestions** – How to improve resume relevance

> ⚠️ Note: The score may feel low because the system focuses on **semantic relevance**, not keyword stuffing.

---

## 🧪 Installation & Setup

```bash
# Clone repository
git clone https://github.com/pmittal1805/Ai_Resume_Jd.git
cd Ai_Resume_Jd

# Create virtual environment
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 📌 Use Cases

* AI/ML Internship Screening
* Resume Optimization
* Career Guidance Tools
* ATS (Applicant Tracking System) Simulation

---

## 🧠 Interview Explanation (How to Say It)

> “This project uses transformer-based sentence embeddings to compare resumes with job descriptions semantically. Instead of relying only on keyword matching, it calculates cosine similarity between embeddings and identifies missing skills using a predefined skill dictionary.”

---

## 🔮 Future Improvements

* Auto skill extraction using NER
* Resume section-wise scoring
* Multi-JD comparison
* Resume rewriting suggestions using LLMs
* Database support for multiple users

---

## 👤 Author

**Mittal Panchal**
AI/ML & NLP Enthusiast

GitHub: [https://github.com/pmittal1805](https://github.com/pmittal1805)

---

## ⭐ If this project helped you

Give it a ⭐ on GitHub and feel free to fork or improve it.
