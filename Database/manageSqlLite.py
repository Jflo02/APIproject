import sqlite3


class ManageSqlLite:
    def __init__(self, databaseName):
        self.sqlConnection = sqlite3.connect(databaseName)
        self.sqlCursor = self.sqlConnection.cursor()

    def executeSqlCommande(self, sqlCmd):
        self.sqlCursor.execute(sqlCmd)

    def executeSqlScript(self, sqlScript):
        self.sqlCursor.executescript(sqlScript)

    def commmit(self):
        self.sqlConnection.commit()

    def closeConnection(self):
        self.sqlConnection.close()