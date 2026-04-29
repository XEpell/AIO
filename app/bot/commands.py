from app.bot.commands import handle_command, state


def get_bot_response(message: str) -> str:
    # 1. проверка команды
    command_result = handle_command(message)
    if command_result:
        return command_result

    # 2. если режим памяти включен — сохраняем
    if state.memory_mode:
        state.add_to_memory(message)
        return "Saved to memory"

    # 3. обычный ответ с учетом памяти
    memory_context = state.get_memory_context()

    if memory_context:
        return f"[Using memory]\n{memory_context}\n---\nEcho: {message}"

    return f"Echo: {message}"