# บทที่ 10 เปลี่ยนโครงสร้างเป็น Clean Architecture

## ลบ __pycache__
```
rmdir /s /q __pycache__
```

## คำสั่งรัน
```
python run.py
```

## สร้าง virtualenv
```
python -m venv _env
```

## .env
```.env
SQLALCHEMY_DATABASE_URI = "sqlite:///School.db"
```