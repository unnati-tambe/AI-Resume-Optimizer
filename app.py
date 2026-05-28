import streamlit as st
import plotly.express as px
import pandas as pd

from resume_parser import extract_text_from_pdf

from nlp_analyzer import calculate_match
from nlp_analyzer import missing_skills

from ai_suggestions import get_ai_suggestions


st.set_page_config(
    page_title="AI Resume Optimizer",
    layout="wide"
)


st.title("AI Resume Optimizer")
st.markdown(
    "### Optimize your resume using AI and ATS analysis"
)

uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description"
)


if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    score = calculate_match(
        resume_text,
        job_description
    )

    missing = missing_skills(
        resume_text,
        job_description
    )

    st.success("Resume uploaded successfully!")

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            "ATS Score",
            f"{score}%"
        )

    with kpi2:
        st.metric(
            "Missing Skills",
            len(missing)
        )

    with kpi3:
        st.metric(
            "Matched Skills",
            max(0, 100 - len(missing))
        )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("ATS Match Score")

        st.metric(
            label="Score",
            value=f"{score}%"
        )

        if score >= 80:

            st.success("Excellent Resume Match")

        elif score >= 60:

            st.warning("Good Resume Match")

        else:

            st.error("Needs Improvement")

    with col2:

        st.subheader("Missing Skills")

        st.write(missing)
        matched_skills = max(0, 100 - len(missing))

    chart_data = pd.DataFrame({
        "Category": ["Matched Skills", "Missing Skills"],
        "Value": [matched_skills, len(missing)]
    })

    fig = px.pie(
        chart_data,
        names="Category",
        values="Value",
        title="Resume Skill Analysis"
    )

    st.plotly_chart(fig)
    tab1, tab2, tab3 = st.tabs(
        ["Insights", "Resume Text", "Suggestions"]
    )

    with tab1:

        if score >= 80:

            st.success(
                "Excellent ATS Match"
            )

        elif score >= 60:

            st.warning(
                "Good Match but needs improvement"
            )

        else:

            st.error(
                "Resume needs optimization"
            )

        st.write("Missing Skills:")

        if missing:

            for skill in missing[:10]:

                st.markdown(
                    f"""
                    <span style="
                    background-color:#ff4b4b;
                    padding:6px;
                    border-radius:8px;
                    color:white;
                    margin:4px;
                    display:inline-block;">
                    {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success("No major missing skills")

    with tab2:

        st.write(resume_text)

    with tab3:

        suggestions = get_ai_suggestions(
            resume_text,
            job_description
        )

        for suggestion in suggestions:

            st.info(suggestion)

        report = f"""
AI Resume Optimization Report

ATS Match Score:
{score}%

Missing Skills:
{missing}

AI Suggestions:
{suggestions}
"""

        st.download_button(
            label="Download Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain"
        )