from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
#import pandas as pd


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content([prompt[0], question])
    return response.text


prompt = [
    """
    You are an expert of data engineering . 
    Answer correctly based on latest information you have.
    """
]

def gemini_model_call(question):
    response = get_gemini_response(question, prompt)
    return response