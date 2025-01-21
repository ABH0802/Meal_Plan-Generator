import os
from cerebras.cloud.sdk import Cerebras

client = Cerebras(
    ""
)

message_log = []


def make_api_call():
    return client.chat.completions.create(
    messages=message_log,
    model="llama3.1-8b",
    )

message_log = [
    {
        "role": "system",
        "content": "You are an AI that generates a meal plan based on Age, Weight, Height, and Activity Level. Then generate a meal plan based on that. Do not put ingredients (US measurements)",
    }
]


while(True):
    i = input("Enter your details here (age, height (in), weight (lbs), activity level, and dietary restrictions (veg, nonveg, etc)):")
    message_log.append(
        {
        "role": "user",
        "content": i,
        }
    )
    response = make_api_call()
    print(response.choices[0].message.content)
    message_log.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }
    )
