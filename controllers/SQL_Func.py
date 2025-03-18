import mysql.connector

def __init__(self):
    self.cursor = mysql.connector.connect().cursor()



def startApp(self):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tourfirm"
        )
        self.cursor = db.cursor()
        #print(db)
    except ValueError as e:
        #print(e)
        pass


def auth(login, password):
    query = ('''SELECT login, password FROM Clients WHERE login =(?) AND password =(?)''',
             (login, password))
    #cursor.execute()