# llm.py uses OpenAI's API to generate answers to the respective prompts
# https://platform.openai.com/docs/quickstart?api-mode=responses
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content