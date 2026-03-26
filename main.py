from agent.core import run_agent

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    response = run_agent(user_input)
    print("Agent: ", response)