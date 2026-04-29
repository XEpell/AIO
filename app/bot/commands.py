from app.bot.state import state  # ВАЖНО: общий объект

def handle_command(text: str):
    text = text.strip().lower()

    if text == "/memory_start":
        state.start_memory()
        return "Memory mode ON"

    if text == "/memory_stop":
        state.stop_memory()
        return "Memory saved & cleaned"

    if text == "/memory_clean":
        state.memory = state.memory  # можно заменить на clean_memory если нужно
        return "Memory cleaned"

    return None