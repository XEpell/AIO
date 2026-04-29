from app.bot.commands import handle_command
from app.bot.state import state


def get_bot_response(message: str) -> str:
    command_result = handle_command(message)
    if command_result:
        return command_result

    if state.memory_mode:
        state.add_to_memory(message)
        return "Saved to memory"

    memory_context = state.get_memory_context()

    if memory_context:
        return f"[Memory]\n{memory_context}\n---\nEcho: {message}"

    return f"Echo: {message}"