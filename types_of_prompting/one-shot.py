import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key= os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1",

)


response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": """Translate the given English sentence into Hindi.
            Example:
                English: Good morning, how are you?
                Hindi: सुप्रभात, आप कैसे हैं?          
            """
        },
        {
            "role": "user",
            "content": "ill definetly get succeded and ill get a job in microsoft or google"
        }
    ]
)

print(response.choices[0].message.content)