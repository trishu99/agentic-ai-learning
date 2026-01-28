from openai import OpenAI

client = OpenAI()

prompt = "Explain AI in one sentence."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

print(response.choices[0].message.content)
