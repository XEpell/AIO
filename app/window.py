from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from app.widgets.chat_view import ChatView
from app.widgets.input_box import InputBox
from app.bot.logic import get_bot_response


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat App")

        self.chat_view = ChatView()
        self.input_box = InputBox()

        self.input_box.message_sent.connect(self.handle_message)

        central_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.chat_view)
        layout.addWidget(self.input_box)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # защита от реентерации (важно для стабильности Qt)
        self._lock = False

    def handle_message(self, text: str):
        if self._lock:
            return

        self._lock = True
        try:
            text = text.strip()
            if not text:
                return

            self.chat_view.add_message("You", text)

            response = get_bot_response(text)

            self.chat_view.add_message("Bot", response)

        finally:
            self._lock = False