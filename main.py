from agent.core import run_agent

print("AI Agent Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = run_agent(user_input)
    print("Agent:", response)

    