import PyQt6
from PyQt6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TourFirm")
        self.window_width, self.window_height = 800, 500
        self.setFixedSize(self.window_width, self.window_height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)



