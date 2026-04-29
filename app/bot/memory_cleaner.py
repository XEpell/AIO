import re


def is_valid_line(text: str) -> bool:
    text = text.strip()

    # слишком короткие
    if len(text) < 3:
        return False

    # только символы/мусор
    if not re.search(r"[a-zA-Zа-яА-Я0-9]", text):
        return False

    return True


def clean_memory(memory: list) -> list:
    seen = set()
    cleaned = []

    for item in memory:
        item = item.strip()

        if not is_valid_line(item):
            continue

        # удаление дублей (регистронезависимо)
        key = item.lower()
        if key in seen:
            continue

        seen.add(key)
        cleaned.append(item)

    return cleaned