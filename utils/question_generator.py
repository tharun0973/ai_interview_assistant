# utils/question_generator.py
import subprocess

def generate_questions(skills, role, difficulty='medium'):
    prompt = f"Generate 3 {difficulty} interview questions for a {role} based on these skills: {', '.join(skills)}"
    result = subprocess.run(
        ["ollama", "run", "tinyllama", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
