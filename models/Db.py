import pymysql


class Db:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            db="users",
            cursorclass=pymysql.cursors.DictCursor
        )

    def _get_connection(self):
        return self.__connection
