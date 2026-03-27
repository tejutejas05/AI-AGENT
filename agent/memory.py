class Memory:
    def __init__(self):
        self.history = []

    def add(self, user, agent):
        self.history.append({"user": user, "agent": agent})

    def get_context(self):
        context = ""
        for chat in self.history[-5:]:  # last 5 messages
            context += f"User: {chat['user']}\nAgent: {chat['agent']}\n"
        return context