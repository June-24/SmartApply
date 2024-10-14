import streamlit as st
from chain import Chain
from utils import extract_resume_text, clean_text
from job import display_job_info, display_skills, display_projects, display_email, display_improvements
from langchain_community.document_loaders import WebBaseLoader

def create_streamlit_app(llm):
    st.write("## SmartApply: Resume Analyzer and Application Helper")
    
    resume_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
    job_url = st.text_input("Enter Job Portal URL:")
    
    responses_generated = False
    
    if st.button("Generate Responses"):
        if resume_file and job_url:
            # Extract resume text
            resume_text = extract_resume_text(resume_file)
            Resume_cleaned_text = clean_text(resume_text)
            
            # Scrape job data
            loader = WebBaseLoader([job_url])
            job_data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(job_data)

            # Store responses in session state
            if 'responses' not in st.session_state:
                st.session_state.responses = {}
                st.session_state.jobs_info = []

            st.session_state.responses.clear()
            print(jobs)
            for job in jobs:
                skills = job.get('skills', [])
                st.session_state.responses['cold_email'] = llm.write_mail(job['description'], Resume_cleaned_text)
                st.session_state.responses['recommended_skills'] = llm.recommend_skills(Resume_cleaned_text, job)
                st.session_state.responses['recommended_projects'] = llm.recommend_projects(job)
                st.session_state.responses['improvement_suggestions'] = llm.improve_resume(Resume_cleaned_text)

                job_info = {
                    "role": job.get('role', 'N/A'),
                    "experience": job.get('experience', 'N/A'),
                    "skills": ', '.join(skills),
                    "description": job.get('description', 'N/A')
                }
                st.session_state.jobs_info.append(job_info)

            responses_generated = True

    if 'responses' in st.session_state and st.session_state.responses:
        st.success("✔ Responses generated successfully!")
        responses_generated = True

    if responses_generated:
        display_job_info()
        display_skills()
        display_projects()
        display_email()
        display_improvements()


if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="SmartApply", page_icon="📧")
    create_streamlit_app(chain)
