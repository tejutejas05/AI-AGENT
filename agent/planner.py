from llm.gemini_client import ask_llm

def decide_action(user_input, context):
    
    prompt = f"""
You are an AI agent planner.

Decide the action based on user input.

Available tools:
1. calculator → for math
2. time → for current time
3. general → for normal questions

Return ONLY one word:
calculator / time / general

Context:
{context}

User: {user_input}
"""

    decision = ask_llm(prompt).strip().lower()
    return decision