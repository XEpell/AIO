from PyQt6.QtWidgets import QTextEdit


class ChatView(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)

    def add_message(self, sender: str, message: str):
        self.append(f"<b>{sender}:</b> {message}")