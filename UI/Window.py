import PyQt6
from PyQt6.QtWidgets import QMainWindow, QPushButton, QGridLayout


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TourFirm")
        self.setFixedSize(600, 600)

        self.lay = QGridLayout()
        self.setLayout(self.lay)



