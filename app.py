from convert import ExtractPDFText 
from ATS_score import calculateATSscore
from model import modelFeedback
import streamlit as st 
import time

# Initialize session state
if "page_number" not in st.session_state:
    st.session_state.page_number = 1

st.title("AI-Powered ATS Screening")

# Initialize variables
resume_data = ""
jobdescription = ""

def page1():
    global resume_data  # Use the global variable
    pdf = st.file_uploader(label="Upload your resume", type="pdf")

    if pdf:
        st.success("Resume uploaded successfully.")
        resume_data = ExtractPDFText(pdf)
        st.write("done")

def page2():
    global jobdescription
    st.title("Enter Job Description")
    jobdescription = st.text_area("Job Description: ")
    submit = st.button("Submit")

    if submit:
        start()

def start():
    global resume_data, jobdescription
    if resume_data and jobdescription:
        # st.write("hi")
        st.subheader("AI FEEDBACK:")
        ATS_score = calculateATSscore("My Resume.pdf", jobdescription)
        model_feedback = modelFeedback(ATS_score, resume_data)
        st.write(model_feedback.text)

page1()
page2()
