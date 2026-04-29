class BotState:
    def __init__(self):
        self.memory_mode = False
        self.memory = []

    def start_memory(self):
        self.memory_mode = True

    def stop_memory(self):
        self.memory_mode = False

    def add_to_memory(self, text: str):
        self.memory.append(text)

    def get_memory_context(self) -> str:
        return "\n".join(self.memory)