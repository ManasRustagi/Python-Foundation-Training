from mysql import connector
import mysql


class DBUtil:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None


    def getDBConnection(self):
        return self.con.cursor()
