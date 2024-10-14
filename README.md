# SmartApply: AI-Powered Resume Analyzer and Application Generator

**SmartApply** is an AI-based tool designed to simplify job applications. It allows users to upload their resume and a job portal link, then generates personalized recommendations, such as a cold email, suggested skills, relevant projects, and resume improvement tips.
Access it here: [link](to be added)

## Features
- **Resume Text Extraction:** Automatically extracts text from a PDF resume.
- **Job Post Scraping:** Scrapes job details from a provided job portal URL.
- **Cold Email Generation:** Creates a professional, role-specific cold email for job applications.
- **Recommended Skills:** Suggests new skills based on the job description and the user's resume.
- **Project Suggestions:** Recommends relevant projects to help users build their portfolio.
- **Resume Improvement Tips:** Provides feedback on areas to enhance in the resume.

## Installation

1. **Clone the repository**
   
2. **Create a virtual environment and activate it**
  
3. **Install required dependencies**
   
4. **Set up environment variables:**
   - Create a `secrets.toml` file in the `.streamlit` directory to store the Groq API key (or store them in .env file ).

    ```
    [GROQ]
    API_KEY = "your_groq_api_key_here"
    ```

## Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Use the UI:**
   - Upload your resume (PDF format).
   - Enter the URL of a job portal with job postings.
   - Click "Generate Responses" to receive tailored suggestions.

## Contributing
Feel free to submit issues or pull requests for improvements.

