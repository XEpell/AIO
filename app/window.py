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

    def handle_message(self, text: str):
        self.chat_view.add_message("You", text)

        response = get_bot_response(text)

        self.chat_view.add_message("Bot", response)