import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(prompt):
    response = model.generate_content(prompt)
    return response.text


    