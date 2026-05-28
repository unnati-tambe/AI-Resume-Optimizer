def get_ai_suggestions(resume_text, job_description):

    suggestions = []

    resume = resume_text.lower()

    jd = job_description.lower()

    skills = [
        "sql",
        "python",
        "excel",
        "power bi",
        "tableau",
        "machine learning",
        "data analysis"
    ]

    for skill in skills:

        if skill in jd and skill not in resume:

            suggestions.append(
                f"Add {skill} skills or projects to your resume."
            )

    suggestions.append(
        "Use more action verbs like analyzed, developed, created."
    )

    suggestions.append(
        "Add measurable achievements with numbers and results."
    )

    return suggestions