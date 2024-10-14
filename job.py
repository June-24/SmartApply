import streamlit as st

def display_job_info():
    if st.button("Show Job Information"):
        if 'jobs_info' in st.session_state and st.session_state.jobs_info:
            for job in st.session_state.jobs_info:
                st.write(f"**Position:** {job['role']}")
                st.write(f"**Experience:** {job['experience']}")
                st.write(f"**Skills:** {job['skills']}")
                st.write(f"**Description:** {job['description']}\n")
        else:
            st.warning("No job information available.")

def display_skills():
    if st.button("Recommended Skills"):
        if 'responses' in st.session_state:
            st.write(st.session_state.responses.get('recommended_skills', 'No response generated.'), language='markdown')
        else:
            st.warning("Please generate responses first.")

def display_projects():
    if st.button("Recommended Projects"):
        if 'responses' in st.session_state:
            st.write(st.session_state.responses.get('recommended_projects', 'No response generated.'), language='markdown')
        else:
            st.warning("Please generate responses first.")

def display_email():
    if st.button("Sample Email"):
        if 'responses' in st.session_state:
            st.write(st.session_state.responses.get('cold_email', 'No response generated.'), language='markdown')
        else:
            st.warning("Please generate responses first.")

def display_improvements():
    if st.button("Improvements and Suggestions"):
        if 'responses' in st.session_state:
            st.write(st.session_state.responses.get('improvement_suggestions', 'No response generated.'), language='markdown')
        else:
            st.warning("Please generate responses first.")
