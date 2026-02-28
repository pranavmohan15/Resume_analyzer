from sentence_transformers import SentenceTransformer, util
import re

model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_years(text):
    matches = re.findall(r'(\d+)\s+years', text.lower())
    return max([int(x) for x in matches], default=0)
def extract_required_years(text):
    match = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*years', text.lower())
    if match:
        return int(match.group(2))
    return extract_years(text)


def calculate_similarity(resume_text, job_text):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb1, emb2).item()
    return max(0, similarity * 100)


def advanced_score(resume_text, job_text, extract_skills_func):

    resume_skills = set(extract_skills_func(resume_text))
    job_skills = set(extract_skills_func(job_text))

    # 1️⃣ Weighted Skill Score (50%)
    core_weight = 3
    secondary_weight = 1

    total_weight = 0
    matched_weight = 0

    for skill in job_skills:
        weight = core_weight if skill in ["python", "django", "mysql"] else secondary_weight
        total_weight += weight
        if skill in resume_skills:
            matched_weight += weight

    skill_score = (matched_weight / total_weight) * 100 if total_weight else 0

    # 2️⃣ Mandatory Skill Penalty
    mandatory_skills = ["python", "django"]
    missing_mandatory = [s for s in mandatory_skills if s not in resume_skills]
    penalty = 20 * len(missing_mandatory)

    # 3️⃣ Semantic Score (20%)
    semantic_score = calculate_similarity(resume_text, job_text)

    # 4️⃣ Experience Score (15%)
    resume_years = extract_years(resume_text)
    required_years = extract_required_years(job_text)
    if required_years:
        if resume_years == 0:
            experience_score = 70   # Fresher fallback
        else:
            experience_score = min(resume_years / required_years, 1) * 100
    else:
        experience_score = 100
    # 5️⃣ Skill Depth Score (15%)
    depth_score = 0
    for skill in job_skills:
        count = resume_text.lower().count(skill.lower())
        if count >= 3:
            depth_score += 5
        elif count >= 1:
            depth_score += 2

    depth_score = min(depth_score, 100)
    

    # Final Score
    final_score = (
       0.65 * skill_score +
       0.15 * semantic_score +
       0.10 * experience_score +
       0.10 * depth_score
    ) - penalty
    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)
    print("Matched Weight:", matched_weight)
    print("Skill Score:", skill_score)
    print("Semantic Score:", semantic_score)
    print("Experience Score:", experience_score)
    print("Depth Score:", depth_score)
    print("Penalty:", penalty)

    return round(max(0, min(final_score, 100)), 2)
