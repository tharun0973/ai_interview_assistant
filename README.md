 🧠 AI Interview Preparation Assistant

A resume-aware, role-specific interview simulator powered by local LLMs. Upload your resume, select a target role, and practice answering personalized questions with real-time feedback — all offline using TinyLlama via Ollama.

---

## 🛠️ Tech Stack

- **Python** — Core logic and modular architecture  
- **Streamlit** — Interactive UI  
- **pdfplumber** — Resume parsing  
- **TinyLlama via Ollama** — Local LLM for question generation and feedback  
- **Regex + NLP** — Skill extraction from resume  

---

## 📦 Features

- 📄 Upload resume (PDF)  
- 🧠 Extract skills using NLP  
- 🎯 Select target role and difficulty  
- 🤖 Generate personalized interview questions  
- 💬 Answer interactively and receive feedback  
- 🔒 No API keys required — fully offline  

---

## 📁 Folder Structure

\`\`\`
ai_interview_assistant/
├── app.py
├── requirements.txt
├── .gitignore
├── utils/
│   ├── resume_parser.py
│   ├── question_generator.py
│   ├── answer_evaluator.py
├── assets/
│   └── styles.css
├── examples/
│   └── sample_resume.pdf
\`\`\`

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
\`\`\`bash
git clone https://github.com/tharun0973/ai_interview_assistant.git
cd ai_interview_assistant
\`\`\`

### 2. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Pull TinyLlama (via Ollama)
\`\`\`bash
ollama pull tinyllama
\`\`\`

### 4. Run the App
\`\`\`bash
streamlit run app.py
\`\`\`

---

## 🧠 Model Notes

This app uses [TinyLlama](https://ollama.com/library/tinyllama) via [Ollama](https://ollama.com) for local LLM inference. No cloud dependency, no API keys, and works offline.

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🙌 Credits

Built by [Tharun Kumar](https://github.com/tharun0973) — AI Engineer 
