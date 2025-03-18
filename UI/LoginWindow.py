from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel

from UI.Window import Window
from services.LoginWindow import registrationUser


class LoginWindow(Window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TourFirm Auth")

        logint_txt = QLabel("Login")
        login = QLineEdit('')

        password_txt = QLabel("Password")
        password = QLineEdit('')
        password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_auth = QPushButton("Вход",clicked=lambda: registrationUser(login.text(),password.text() ) )

        self.layout.addWidget(logint_txt, 0, 0)
        self.layout.addWidget(login, 0, 1)
        self.layout.addWidget(password_txt, 1, 0)

        self.layout.addWidget(password, 1, 1)
        self.layout.addWidget(btn_auth, 2, 1)
