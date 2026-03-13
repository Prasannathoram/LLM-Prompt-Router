import json
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def classify_intent(message: str):

    prompt = f"""
Classify the user's intent.

Choose ONLY from these labels:
code, data, writing, career, unclear

Return ONLY valid JSON. No explanation, no extra text.

Example:
{{"intent":"code","confidence":0.92}}

User message:
{message}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0,
            messages=[
                {"role": "system", "content": "You are a strict JSON generator."},
                {"role": "user", "content": prompt}
            ]
        )

        text = response.choices[0].message.content.strip()

        # DEBUG (so we can see what the model returned)
        print("\nClassifier raw output:", text)

        # Extract JSON safely
        match = re.search(r'\{.*\}', text, re.DOTALL)

        if match:
            return json.loads(match.group())

        return {"intent": "unclear", "confidence": 0.0}

    except Exception as e:
        print("Classifier error:", e)
        return {"intent": "unclear", "confidence": 0.0}