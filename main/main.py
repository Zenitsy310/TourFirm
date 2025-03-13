from PyQt6.QtWidgets import QApplication, QWidget

import sys # Только для доступа к аргументам командной строки

from UI.LoginWindow import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаём виджет Qt — окно.
    window = LoginWindow()
    window.show()  # Важно: окно по умолчанию скрыто.


    app.exec()



