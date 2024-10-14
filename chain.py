import streamlit as st
# import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
# from dotenv import load_dotenv
# load_dotenv()

class Chain:
    def __init__(self):
        # using the below one for deploying onto streamlit
        groq_api_key = st.secrets["GROQ"]["API_KEY"]

        # use the below one if using the .env
        # groq_api_key=os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-groq-8b-8192-tool-use-preview")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in 
            JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON. 
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, skills):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            Write a cold email to the HR including the following skills 
            (Strictly follow what is given in skills, dont generate random ones that re not in the resume 
            and they should be relevant to the job description too) from the resume: {skills}.
            The email should be concise and professional. also mention at the end that the resume is attached.
            and thank the recruiter for revieving the application or reading the mail.
            MAX 400 WORDS 
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "skills": skills})
        return res.content

    def recommend_skills(self, resume_text, job):
        prompt_skills = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            ### RESUME TEXT:
            {resume_text}

            ### INSTRUCTION:
            Above are both the job description and the resume 
            now based on the job description generate what all skills the user needs to add to their resume 
            keywords and in markdown (dont give skills that are already in resume, give relevant to job data)
            MAX 5 SKILLS NOT MORE (Markdown)
            ### RECOMMENDED SKILLS (NO PREAMBLE):
            """
        )
        chain_skills = prompt_skills | self.llm
        res = chain_skills.invoke({"job_description": str(job),"resume_text": resume_text})
        return res.content

    def recommend_projects(self, job_Description):
        prompt_projects = PromptTemplate.from_template(
            """
            ### RESUME TEXT:
            {job_Description}

            ### INSTRUCTION:
            Above is a json file containing the skills description role and exeprience required for this position
            give recommendation to 5 different projects that would help with applying to this role and be similar to the skills needed
            MAX 5 PROJECTS (Markdown)
            ### RECOMMENDED PROJECTS (NO PREAMBLE):
            """
        )
        chain_projects = prompt_projects | self.llm
        res = chain_projects.invoke({"job_Description": job_Description})
        return res.content

    def improve_resume(self, resume_text):
        prompt_improve = PromptTemplate.from_template(
            """
            ### RESUME TEXT:
            {resume_text}

            ### INSTRUCTION:
            Provide recommendations to improve the resume.
            tell the places where requirements are needed
            MAX 5 IMPROVEMENTS (POINTWISE) (Markdown)
            ### IMPROVEMENT SUGGESTIONS (NO PREAMBLE):
            """
        )
        chain_improve = prompt_improve | self.llm
        res = chain_improve.invoke({"resume_text": resume_text})
        return res.content