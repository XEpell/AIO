from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSignal


class InputBox(QWidget):
    message_sent = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.input = QLineEdit()
        self.send_button = QPushButton("Send")

        layout = QHBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    def send_message(self):
        text = self.input.text().strip()
        if text:
            self.message_sent.emit(text)
            self.input.clear()