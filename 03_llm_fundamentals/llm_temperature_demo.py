from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "user", "content": "Explain gravity in one sentence"}
    ],
    temperature=0.0
)

print(response.choices[0].message.content)
