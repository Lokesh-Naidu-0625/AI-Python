import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key= os.getenv("GEMINI_API_key"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
    model="gemini-3.8-flash",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": """You are a helpful maths assistant only.
            just answer maths related querys only. 
            if the query is not related to math means just display {sorry i cant process the question} as output"""
        },
        {
            "role": "user",
            "content": "can you solve the a+b whole square"
        }
    ]
)

print(response.choices[0].message.content)