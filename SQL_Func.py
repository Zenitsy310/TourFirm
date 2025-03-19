import mysql.connector


class sql_work():
    cursor = None

    @classmethod
    def startApp(cls):
        try:
            db = mysql.connector.connect(
                host="localhost", #127.0.0.1
                user="root",
                password="",
                database="tourfirm"
            )
            print(db)
            cls.cursor = db.cursor()


        except ValueError as e:

            pass

    @staticmethod
    def auth(cls, login, password):
        print(cls.cursor.execute('''SELECT * FROM clients''').fetchall())
        # print(cls.cursor.execute('''SELECT * FROM clients''').fetchall())
        pass
