# Brain of the agent (LLM)

from tools.calculator import calculate
# this will import the tools from the tools folder
from tools.time_tool import get_time
from llm.openai_client import ask_llm



# the Prompt template we are going to use for this agent

def run_agent(user_input):

    if "time" in user_input.lower():
        return get_time()

    elif "calculate" in user_input.lower():
        expression = user_input.replace("calculate", "")
        return calculate(expression)

    else:
        return ask_llm(user_input)
        #here the llm folder should be get accessed 


