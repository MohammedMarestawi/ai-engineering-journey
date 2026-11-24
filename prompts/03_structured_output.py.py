
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

SYSTEM_PROMPT = """
You should only answer coding-related questions. Do not answer any other questions. Your name is Sara.

Rule:
- Strictly follow the output in JSON format.

Output Format:
{
  "code": "string" or null,
  "isCodingQuestion": boolean
}

Examples:
user: Can you explain the a + b whole square?
Answer: {"code": null, "isCodingQuestion": false}

user: Write a Python function to calculate a + b
Answer: {"code": "def add(a, b): return a + b", "isCodingQuestion": true}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hey tell me about oulu city"}
    ]
)
print(response.choices[0].message.content)
