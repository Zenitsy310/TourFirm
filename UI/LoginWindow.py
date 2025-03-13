from PyQt6.QtWidgets import QPushButton

from UI.Window import Window


class LoginWindow(Window):
    def __init__(self):
        super().__init__()



        btnAuth = QPushButton("Вход")
        btnAuth.clicked.connect(self.the_button_was_clicked)
        self.layout().addWidget(btnAuth)

