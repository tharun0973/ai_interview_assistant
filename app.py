import streamlit as st
from utils.resume_parser import extract_skills_from_pdf
from utils.question_generator import generate_questions
from utils.answer_evaluator import evaluate_answer

st.title("🧠 AI Interview Preparation Assistant")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
role = st.text_input("Target Job Role", value="Software Engineer")
difficulty = st.selectbox("Difficulty Level", ["easy", "medium", "hard"])

if uploaded_file and role:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    skills = extract_skills_from_pdf("temp_resume.pdf")
    st.success(f"Extracted Skills: {', '.join(skills)}")

    questions = generate_questions(skills, role, difficulty)
    st.subheader("Interview Questions")
    for i, q in enumerate(questions.split('\n'), 1):
        st.markdown(f"**Q{i}:** {q}")
        user_answer = st.text_area(f"Your Answer to Q{i}")
        if user_answer:
            feedback = evaluate_answer(q, user_answer)
            st.markdown(f"📝 **Feedback:** {feedback}")
