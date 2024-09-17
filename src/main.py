from PySide6.QtWidgets import QApplication
from main_widget import MainWidget
from sys import exit


def main():
    app = QApplication([])
    widget = MainWidget()
    widget.resize(200, 200)
    widget.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
