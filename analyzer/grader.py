# grader.py grades uploaded documents/responses
from llm import *
def grade_document(content, rubric):
    prompt = (
        f"Grade this student essay based on the following rubric: {rubric}.\n"
        f"Give a score out of 10 and explain your reasoning:\n{content}"
    )
    return ask_llm(prompt)