import PyQt6
import sys  # Только для доступа к аргументам командной строки

from PyQt6.QtWidgets import QApplication

from UI.LoginWindow import LoginWindow
from controllers import SQL_Func
from controllers.SQL_Func import sql_work

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sql_work.startApp()
    # Создаём виджет Qt — окно.
    window = LoginWindow()
    window.show()  # Важно: окно по умолчанию скрыто.
    app.exec()
