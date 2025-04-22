# llm.py uses OpenAI's API to generate answers to the respective prompts
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt, model="gpt-4", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response['choices'][0]['message']['content']