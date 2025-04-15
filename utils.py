import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

def get_career_guidance(name, education, interests, skills):
    prompt = f"""
    Act as a professional career counselor. Based on the profile below, suggest top 5 career paths, explain why each fits the user, and provide growth tips.

    Name: {name}
    Education: {education}
    Interests: {interests}
    Skills: {skills}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating guidance: {str(e)}"
