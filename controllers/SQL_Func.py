import mysql.connector
from mysql.connector import Error


class sql_work:
    _connection = None
    _cursor = None

    @classmethod
    def startApp(cls):
        try:
            cls._connection = mysql.connector.connect(
                host="localhost",
                user="Kokushibo",
                password="oleg75270",
                database="tourfirm"
            )

            cls._cursor = cls._connection.cursor()
        except Error as e:
            #print(f"Error while connecting to MySQL: {e}")
            pass

    @classmethod
    def auth(cls, login, password):
        cls._cursor.execute("SELECT * FROM client WHERE login = %s AND password = %s", (login, password))
        return cls._cursor.fetchall()



