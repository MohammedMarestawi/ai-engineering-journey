
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Python specialist. Only answer Python-related questions. If a question is not about Python, politely say that you only help with Python coding topics."},
        {"role": "user", "content": "hey"}
    ]
)
print(response.choices[0].message.content)
