import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key= os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1",

)

system_prompt = """
You are a helpful problem-solving assistant.

        For every problem:
        1. Understand the question carefully.
        2. Break the problem into smaller steps.
        3. Work through the necessary calculations or logic or theories.
        4. Provide the final answer clearly.
        5. Keep the explanation concise and easy to understand.

        Do not reveal private internal chain-of-thought.
        Instead, provide a concise explanation of the key steps.
"""
# you can add some examples too so that you are able to know what type of question should answer in which format
# more examples higher the accuracy

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "how to prepare italian cheese pasta"
        }
    ]
)

print(response.choices[0].message.content)