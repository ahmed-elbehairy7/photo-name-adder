from os import listdir
from os.path import join, splitext, split
from file_dialogs import get_images, get_output
from PySide6.QtWidgets import QWidget
from write import write


def start(widget: QWidget):
    images = get_images(widget)[0]
    output_dir = get_output(widget)

    for image in images:
        write(image, join(output_dir, split(image)[-1]), splitext(split(image)[-1])[0])
