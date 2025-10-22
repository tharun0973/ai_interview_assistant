# utils/answer_evaluator.py
import subprocess

def evaluate_answer(question, answer):
    prompt = f"Evaluate this answer to the question:\nQ: {question}\nA: {answer}\nGive a score out of 10 and brief feedback."
    result = subprocess.run(
        ["ollama", "run", "tinyllama", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
