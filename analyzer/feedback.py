# feedback.py generates feedback on the uploaded documents after they are analyzed
# using OpenAI's LLM API, add functionality to provide feedback on: grammar, clarity, structure, how to improve, etc
from llm import *

def provide_feedback(content):
    prompt = f"You are an experienced teacher. Provide constructive feedback on this document:\n{content}"
    return ask_llm(prompt)