import mysql.connector as mysqldb
from mysql.connector.errors import Error


class MysqlDatabaseBase:
    def __init__(self, host: str, username: str, password: str, database: str, port: str = 3306):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        try:
            self.connection = mysqldb.connect(host=self.host, user=self.username, \
                                              password=self.password, port=self.port, database=self.database)
        except Error as e:
            print("connection to db failed due to" + str(e))

    def _get_all_results(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        except Error as e:
            print("unable to fetch the results from database due to" + str(e))
        return results if results is not None and len(results) >= 1 else []

    def show_databases(self):
        db_query = "SHOW DATABASES"
        return self._get_all_results(db_query)

    def show_tables(self):
        db_query = "SHOW TABLES"
        return self._get_all_results(db_query)

    def close(self):
        if self.connection:
            self.connection.close()

