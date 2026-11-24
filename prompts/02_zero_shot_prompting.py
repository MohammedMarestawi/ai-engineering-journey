
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

SYSTEM_PROMPT = "You should only answer coding-related questions. Do not answer any other questions. Your name is Sara. If the user asks something other than coding, just say: sorry ;("
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hey tell me about oulu city"}
    ]
)
print(response.choices[0].message.content)
