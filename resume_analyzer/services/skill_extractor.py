import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = [

    # ======================
    # Programming Languages
    # ======================
    "python", "java", "c", "c++", "c#", "javascript",
    "typescript", "go", "ruby", "php", "r", "scala",

    # ======================
    # Backend Development
    # ======================
    "django", "flask", "fastapi",
    "spring", "spring boot",
    "node.js", "express",
    "rest", "rest api", "graphql",
    "microservices",

    # ======================
    # Frontend Development
    # ======================
    "react", "angular", "vue",
    "html", "css", "bootstrap",

    # ======================
    # Databases
    # ======================
    "mysql", "postgresql", "mongodb",
    "sqlite", "oracle", "redis",
    "firebase",

    # ======================
    # DevOps & Cloud
    # ======================
    "aws", "azure", "gcp",
    "docker", "kubernetes",
    "jenkins", "ci/cd",
    "linux", "nginx", 

    # ======================
    # Data Analysis
    # ======================
    "pandas", "numpy",
    "matplotlib", "seaborn",
    "excel", "power bi", "tableau",
    "data cleaning", "data visualization",
    "data analysis", "statistics",

    # ======================
    # Machine Learning
    # ======================
    "machine learning",
    "deep learning",
    "nlp",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "xgboost",

    # ======================
    # Big Data
    # ======================
    "hadoop", "spark",

    # ======================
    # Tools
    # ======================
    "git", "github", "gitlab",
    "jira", "postman",
    "jupyter", "anaconda"
]


import re

def extract_skills(text):
    text = text.lower()

    skills_list = [
        "python", "django", "mysql", "react", "rest api",
        "git", "html", "css", "javascript", "node.js",
        "mongodb", "postman"
    ]

    found = []

    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)

    return found