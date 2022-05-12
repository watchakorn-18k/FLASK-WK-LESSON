# บทที่ 6

### 🛑 คำสั่ง sqlite


คำสั่ง Query ข้อมูลหรือดึงข้อมูลจากฐานข้อมูล
```
import sqlite3
db_local = 'DB.db'
connect = sqlite3.connect(db_local)
cursor = connect.cursor()
cursor.execute("select * from ตาราง")
cursor.fetchall()
```

คำสั่งเพิ่มข้อมูลงในฐานข้อมูล
```
import sqlite3
db_local = 'DB.db'
connect = sqlite3.connect(db_local)
cursor = connect.cursor()
cursor.execute(f"insert into ListStudent (ชื่อคอลัมภ์1,ชื่อคอลัมภ์2,ชื่อคอลัมภ์3) values ('ค่า1','ค่า2','ค่า3')")
connect.commit()
connect.close()
```

### 🛑 คำสั่ง request

```
from flask import request

request.form.get("ชื่อใน form ") เช่น

<input name="First_Last" >

request.form.get("First_Last")
```

