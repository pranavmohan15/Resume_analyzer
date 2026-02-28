# JobFit – Intelligent Resume Analyzer

## Overview

JobFit is an AI-powered resume analysis platform that evaluates how well a resume matches a given job description.

It combines structured skill extraction, semantic similarity using embeddings, experience analysis, and adaptive scoring to generate a realistic match percentage and identify missing skills.

Built using Django, NLP, and Sentence Transformers.

---

## Features

- Resume upload (PDF and DOCX support)
- Automatic resume text extraction
- Skill detection using NLP
- Semantic similarity using Sentence Transformers
- Experience detection and comparison
- Adaptive scoring
- Missing skill identification
- Clean enterprise-style UI
- Django Admin panel

---

## Tech Stack

### Backend
- Python
- Django
- MySQL

### NLP & AI
- spaCy
- Sentence Transformers
- PyTorch

### Frontend
- Bootstrap 5
- Custom CSS

---

## How It Works

1. User registers and logs in
2. Uploads resume (PDF or DOCX)
3. Enters job position, company name, and job description
4. System extracts resume text and detects skills
5. Embeddings are generated for semantic comparison
6. Final score is calculated using:
   - Weighted skill match
   - Semantic similarity
   - Experience score
   - Skill depth score
   - Mandatory skill penalties
7. Match percentage and missing skills are displayed

---

## Scoring Logic

The final score is calculated using adaptive weighting:

- Skill Match Score
- Semantic Similarity Score
- Experience Score
- Skill Depth Score
- Penalty for missing mandatory skills

The system dynamically adjusts scoring weights depending on how detailed the job description is.

---

## Installation

### 1. Clone the Repository

    git clone https://github.com/yourusername/jobfit.git
    cd jobfit

### 2. Create Virtual Environment

Mac/Linux:

    python -m venv env
    source env/bin/activate

Windows:

    python -m venv env
    env\Scripts\activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Install NLP Dependencies

    pip install torch --index-url https://download.pytorch.org/whl/cpu
    pip install sentence-transformers
    pip install spacy
    python -m spacy download en_core_web_sm

### 5. Configure Database

Update database settings in `settings.py`.

### 6. Run Migrations

    python manage.py makemigrations
    python manage.py migrate

### 7. Create Superuser

    python manage.py createsuperuser

### 8. Run Server

    python manage.py runserver

Open in browser:

    http://127.0.0.1:8000/

---

## Future Improvements

- Resume improvement suggestions using LLMs
- Recruiter dashboard
- Candidate ranking system
- REST API integration
- Cloud deployment

---

## Author

Pranav Mohan  
Full Stack Developer | AI Enthusiast
