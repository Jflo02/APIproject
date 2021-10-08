from manageSqlLite import ManageSqlLite

sql = ManageSqlLite("EasySav.db")
sqlCreateTable=f"CREATE TABLE IF NOT EXISTS intervention"\
                f"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"\
                f""\
                f""