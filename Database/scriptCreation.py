from manageSqlLite import ManageSqlLite

sql = ManageSqlLite("EasySav.db")

sqlCreateTable = open("scriptbddAPI.txt", "r")

sql.executeSqlScript(sqlCreateTable.read())
sqlCreateTable.close()
sql.commmit()
sql.closeConnection()
