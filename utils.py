
import os
import PyPDF2
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Extract text from uploaded PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Analyze resume vs job description
def analyze_resume(resume_text, job_desc):
    prompt = f"""
    You are an expert resume reviewer.
    Here is the resume:\n{resume_text}\n
    Here is the job description:\n{job_desc}\n
    Tasks:
    1. Give a match score (0-100).
    2. List missing important keywords.
    3. Suggest specific improvements.
    Format your answer clearly.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
