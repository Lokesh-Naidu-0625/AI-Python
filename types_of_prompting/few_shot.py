import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key= os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1",

)

system_prompt = """you are a emotion detector assistant. 
You will read the sentences and gonna find what are the emotins behind it
Example:
Sentence: "I finally got my dream job!"
Emotion: joyful

Sentence: "They betrayed me. I will seek vengeance on them."
Emotion: anger

Sentence: "I felt so pleasant when i saw my mom's smile "
Emotion: calm

Sentence: "whenever i see her, my heart pumps fast"
Emotion: excitment

Sentence: "finally im at my peace"
Emotion: happy

"""


response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "im gonna break their nose for sure"
        }
    ]
)

print(response.choices[0].message.content)