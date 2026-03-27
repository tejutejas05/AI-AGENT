from agent.memory import Memory
from agent.planner import decide_action
from tools.calculator import calculate
from tools.time_tool import get_time
from llm.gemini_client import ask_llm

memory = Memory()

def run_agent(user_input):

    context = memory.get_context()

    action = decide_action(user_input, context)

    if "calculator" in action:
        expression = user_input.replace("calculate", "")
        result = calculate(expression)

    elif "time" in action:
        result = get_time()

    else:
        prompt = f"{context}\nUser: {user_input}"
        result = ask_llm(prompt)

    memory.add(user_input, result)

    return result