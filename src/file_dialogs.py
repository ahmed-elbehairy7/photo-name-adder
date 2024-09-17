from PySide6.QtWidgets import QFileDialog, QWidget


def get_images(parent: QWidget) -> str:
    return QFileDialog.getOpenFileNames(parent)


def get_output(parent: QWidget):
    return QFileDialog.getExistingDirectory(parent)


if __name__ == "__main__":
    ...
