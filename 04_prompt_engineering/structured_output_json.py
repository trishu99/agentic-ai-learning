
from openai import OpenAI

client = OpenAI()

prompt = """
You are a review classifier.

Classify the following review.

Return ONLY valid JSON in this format:
{
  "label": "POSITIVE | NEGATIVE | NEUTRAL",
  "explanation": "string"
}

Review:
"The product is okay but overpriced."
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

print(response.choices[0].message.content)
