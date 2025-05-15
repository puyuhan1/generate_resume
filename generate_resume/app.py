import streamlit as st
from process_input import process_input
from generate_sections import generate_resume

st.set_page_config(page_title="Qwen Resume Generator", layout="centered")

st.title("📄 AI Resume Generator (Qwen-powered)")
st.write("Paste a short paragraph about your background, and we’ll generate a clean resume for you.")

# User input
user_text = st.text_area("Enter your background description below:")

if st.button("Generate Resume"):
    with st.spinner("Generating..."):
        structured_data = process_input(user_text)
        resume_text = generate_resume(structured_data)

    st.subheader("🎯 Generated Resume")
    st.text(resume_text)
