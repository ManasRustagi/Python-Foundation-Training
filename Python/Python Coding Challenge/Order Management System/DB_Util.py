import mysql.connector
class DBConnector:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None

    def open_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )

    def close_connection(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()