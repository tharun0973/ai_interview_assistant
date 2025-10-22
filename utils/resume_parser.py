import pdfplumber
import re

def extract_skills_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    skills = re.findall(r'\b[A-Za-z]{3,}\b', text)
    keywords = [word.lower() for word in skills if word.lower() in COMMON_SKILLS]
    return list(set(keywords))

COMMON_SKILLS = {
    'python', 'sql', 'aws', 'docker', 'react', 'tensorflow', 'pandas', 'git',
    'linux', 'java', 'c++', 'html', 'css', 'javascript', 'flask', 'django'
}
