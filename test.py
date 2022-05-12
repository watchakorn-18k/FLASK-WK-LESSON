import sqlite3

db_local = 'DB.db'

connect = sqlite3.connect(db_local)
cursor = connect.cursor()
cursor.execute("insert into ListStudent (First_Last,Age,Status) values ('สมชาย สมหญิง',20,'นักเรียน')")
connect.commit()
connect.close()