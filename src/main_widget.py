from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from start import start


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton("start")
        text = QLabel("ضع الكلام على الصور", alignment=Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(text)
        self.layout.addWidget(button)

        button.clicked.connect(lambda: start(self))
