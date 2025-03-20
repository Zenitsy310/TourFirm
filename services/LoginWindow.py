
from controllers.SQL_Func import sql_work


def authUser(login, password):
    #тип проверка полей
    if sql_work.auth(login, password) != None:
        print("kok")
    else:
        pass
    #.auth(login, password)