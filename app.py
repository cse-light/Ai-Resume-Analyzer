
import streamlit as st
from utils import extract_text_from_pdf, analyze_resume
import matplotlib.pyplot as plt
import re

# Streamlit UI settings
st.set_page_config(page_title="📄 AI Resume Analyzer", layout="wide")
st.title("📄 AI Resume Analyzer 🚀")

# Upload resume
uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste the Job Description here")

if uploaded_resume and job_description:
    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
    st.success("Resume text extracted!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            analysis_result = analyze_resume(resume_text, job_description)
        st.subheader("📝 Analysis Result")
        st.markdown(analysis_result)

        # Extract score safely
        try:
            score_match = re.search(r'(\d{1,3})', analysis_result)
            if score_match:
                score = int(score_match.group(1))
            else:
                score = 75
        except:
            score = 75

        st.subheader("📊 Match Score")
        fig, ax = plt.subplots()
        ax.barh(["Match Score"], [score], color="skyblue")
        ax.set_xlim(0, 100)
        st.pyplot(fig)
