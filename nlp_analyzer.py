from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def calculate_match(resume_text, job_description):

    text = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)

 
def extract_keywords(text):

    skills = [

        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "pandas",
        "numpy",
        "matplotlib",
        "statistics",
        "machine learning",
        "data analysis",
        "data visualization",
        "communication",
        "problem solving",
        "teamwork",
        "mysql",
        "postgresql",
        "dashboard",
        "etl",
        "data cleaning",
        "streamlit",
        "nlp",
        "scikit-learn"

    ]

    text = text.lower()

    found_skills = []

    for skill in skills:

        if skill in text:

            found_skills.append(skill)

    return found_skills   


def missing_skills(resume_text, job_description):

    resume_keywords = extract_keywords(resume_text)

    jd_keywords = extract_keywords(job_description)

    missing = []

    for skill in jd_keywords:

        if skill not in resume_keywords:

            missing.append(skill)

    return missing