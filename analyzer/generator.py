# generator.py creates short quizzes, study guides, and other material
# using OpenAI's LLM API, add functionality to generate: multiple choice, true/false, fill in the blank, flashcards, study guides
from analyzer.llm import *

def create_mc(content, number):
    prompt = (
        f"Based on the following content, generate {number} multiple choice questions with answers:\n{content}"
    )
    return ask_llm(prompt)

def create_tf(content, number):
    prompt = (
        f"Based on the following content, generate {number} true or false questions with answers:\n{content}"
    )
    return ask_llm(prompt)

def create_fill(content,number):
    prompt = (
        f"Based on the following content, generate {number} fill in the blank questions with answers:\n{content}"
    )
    return ask_llm(prompt)

def create_fc(content, number):
    prompt = (
        f"Based on the following content, generate {number} flashcard terms with answers:\n{content}"
    )
    return ask_llm(prompt)

def create_sg(content):
    prompt = (
        f"Based on the following content, generate 1 study guide with answers:\n{content}"
    )
    return ask_llm(prompt)