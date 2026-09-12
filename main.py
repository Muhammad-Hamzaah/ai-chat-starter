"""
AI Chat Starter — Project 1
----------------------------
Goal: Samajhna ke LLM API kaise kaam karti hai.
Yeh script user se input leta hai, Google Gemini API ko call karta hai,
aur AI ka response terminal mein show karta hai.

Isay "Hello World" samjho Agentic AI journey ka.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Step 1: .env file se API key load karo (security ke liye key kabhi
# seedha code mein nahi likhte, hamesha .env file mein rakhte hain)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY nahi mili. .env file check karo.")
    exit()

# Step 2: Gemini client banao
client = genai.Client(api_key=api_key)

# Step 3: Chat history rakho (taake AI ko pichli baatein yaad rahein)
chat_history = []


def get_ai_response(user_message: str) -> str:
    """User ka message leta hai, Gemini ko bhejta hai, response return karta hai."""
    chat_history.append(f"User: {user_message}")

    # Poori history ko context ke tor pe bhejte hain
    full_context = "\n".join(chat_history)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=full_context,
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            ),
        ),
    )

    ai_reply = response.text
    chat_history.append(f"AI: {ai_reply}")
    return ai_reply


def main():
    print("=" * 50)
    print("AI Chat Starter — Gemini API Project")
    print("Type 'quit' to exit")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("\nAllah Hafiz!")
            break

        if not user_input:
            continue

        ai_response = get_ai_response(user_input)
        print(f"\nAI: {ai_response}")


if __name__ == "__main__":
    main()