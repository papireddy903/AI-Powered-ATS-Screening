import google.generativeai as genai 
import os
from dotenv import load_dotenv
from convert import ExtractPDFText
load_dotenv()

genai.configure(api_key = os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro") 

def modelFeedback(ats_score,resume_data):

    input_prompt = f"""
        You are now an ATS Score analyzer and given ATS Score is {int(ats_score*100)}%. 
        Your task is to provide feedback to the user based on the ATS score.
        print ATS score first. mention where resume is good and where resume lacks. 
        talk about the resume like one to one chat. 
    """
    response = model.generate_content([input_prompt,resume_data],stream=True)
    response.resolve()

    return response