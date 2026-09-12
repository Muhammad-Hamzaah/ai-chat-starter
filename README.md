# AI Chat Starter

My first step into Agentic AI — a simple command-line chatbot built using
Google's Gemini API to understand how LLM APIs work under the hood.

## What it does

- Takes user input from the terminal
- Sends it to Google Gemini (gemini-2.0-flash model)
- Maintains conversation history so the AI remembers context
- Prints the AI's response back to the user

This is the foundation before moving on to building AI agents that can
take actions (tool calling, RAG, automation workflows).

## Tech Stack

- Python
- Google Gemini API (`google-genai`)
- python-dotenv (for secure API key management)

## Setup

1. Clone this repo
   ```
   git clone <your-repo-url>
   cd ai-chat-starter
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

4. Create a `.env` file (copy `.env.example`) and add your key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```

5. Run it
   ```
   python main.py
   ```

## What I learned

- How to securely handle API keys using environment variables
- How LLM APIs process requests and return responses
- How to maintain conversation context across multiple turns

## What's next

Building on this foundation to create agents that can use tools
(web search, file access, APIs) and eventually full automation workflows.

---
Part of my learning journey into Agentic AI & AI Automation.
