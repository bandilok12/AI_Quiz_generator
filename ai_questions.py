from groq import Groq
from dotenv import load_dotenv
import os
import json
import random

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)

def generate_questions(difficulty):

    prompt = f"""
Generate 10 unique Python foundations
MCQ quiz questions.

Difficulty: {difficulty}

Rules:
1. Return ONLY valid JSON array
2. Each object must contain:
   - question
   - options
   - answer
3. 4 options only
4. answer should be a/b/c/d
5. No repeated questions
6. No explanations

Example:
[
  {{
    "question":"What is Python?",
    "options":["a) Language","b) Snake","c) IDE","d) OS"],
    "answer":"a"
  }}
]
"""

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=1
        )
        content = completion.choices[0].message.content
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()
        questions = json.loads(content)
        random.shuffle(questions)
        return questions

    except Exception as e:
        print("\nError Generating Questions:")
        print(e)
        return []