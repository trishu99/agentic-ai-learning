from openai import OpenAI

client = OpenAI()

prompt = """
Classify the sentiment of this review.
Think step by step before answering.

Review: "The UI is nice but the app crashes often."
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

print(response.choices[0].message.content)
