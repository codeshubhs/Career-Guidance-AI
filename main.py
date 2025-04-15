
import streamlit as st
from utils import get_career_guidance

st.set_page_config(page_title="AI Career Guidance", layout="centered")
st.title("🎯 AI Career Guidance (Gemini AI)")
st.subheader("🔎 Personalized career suggestions based on your profile")

# Form for input
with st.form("career_form"):
    name = st.text_input("👤 Your Name")
    education = st.text_area("🎓 Education Background")
    interests = st.text_area("💡 Your Interests")
    skills = st.text_area("🛠️ Your Skills (comma-separated)")

    submit = st.form_submit_button("Get Career Guidance")

# Show result
if submit:
    if not all([name, education, interests, skills]):
        st.warning("⚠️ Please fill in all fields.")
    else:
        with st.spinner("⏳ Analyzing with Gemini AI..."):
            result = get_career_guidance(name, education, interests, skills)
        st.success("✅ Career Guidance Generated!")
        st.markdown("### 📋 Your Personalized Career Advice:")
        st.write(result)
        st.download_button("📥 Download Guidance", result, file_name="career_guidance.txt") 
        
