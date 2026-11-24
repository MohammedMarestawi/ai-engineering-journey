
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()


client = OpenAI()

SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought.

You work on START, PLAN, and OUTPUT steps.

You need to first PLAN what needs to be done. The PLAN can be multiple steps.

Once you think enough PLAN has been done, finally you can give an OUTPUT

Rules:

Strictly follow the given JSON output format

Only run one step at a time.

The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to

the user).

Output JSON Format:

{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

Example:

START: Hey, Can you solve 2+3*5/10

PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem"

PLAN: { "step": "PLAN": "content": "Looking at the problem, we should solve this using BODMAS method"
PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is the correct thing to do here" 
PLAN: { "step": "PLAN": "content": "First we must multiply 3*5 which is 15"
PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 /10"}
PLAN: { "step": "PLAN": "content": "We must perform divide that is 15/10 = 1.5"}
PLAN: { "step": "PLAN": "content": "Now finally let's perform the add 3.5" } 
PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
OUTPUT: { "step": "OUTPUT": "content": "3.5" }



"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={
        "type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        
        {"role": "user", "content": "hey, write code to add n numbers in js"},
       
       {"role": "assistant", "content": 
        json.dumps({"step": "START", "content": "You want a JavaScript code to add n numbers."})},
       
       { "role": "assistant", "content": 
        json.dumps({ "step": "PLAN", "content": "To create a code that adds n numbers,"
       " we need to determine how to accept n numbers and then sum them up."})},
       { "role": "assistant", "content": 
        json.dumps({"step": "PLAN", "content": 
        "We can use an array tostore the n numbers and then use a loop or the reduce method to find the sum."})},
       { "role": "assistant", "content": 
        json.dumps({"step": "PLAN", "content": "Let's choose to use the reduce method, which is a clean and efficient way to sum the numbers in the array."})},
       { "role": "assistant", "content": 
        json.dumps({"step": "PLAN", "content": "I will write a function that takes an array of numbers as an argument and returns the sum of those numbers using the reduce method."})},

        

    ]
)
print(response.choices[0].message.content)
