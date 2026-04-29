from app.bot.memory_storage import save_memory, load_memory
from app.bot.memory_cleaner import clean_memory

state = {}
class BotState:
    def __init__(self):
        self.memory_mode = False
        self.memory = load_memory()

    def start_memory(self):
        self.memory_mode = True

    def stop_memory(self):
        self.memory_mode = False
        self.memory = clean_memory(self.memory)
        save_memory(self.memory)  # сохраняем только здесь

    def add_to_memory(self, text: str):
        self.memory.append(text)  # БЕЗ I/O

    def get_memory_context(self) -> str:
        return "\n".join(self.memory)