# บทที่ 16 ปรับปรุงระบบ login ด้วย Supabase ตรวจสอบสิทธิ์ผ่านอีเมลและ Google Login


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

## Install requrement
```
pip install -r requirements.txt
```

## .env
```.env
SQLALCHEMY_DATABASE_URI = "postgresql://postgres.x................"
AWS_ACCESS_KEY = ...........
AWS_SECRET_KEY = ..........
BUCKET_NAME = .......
SUPABASE_URL_DATA=........
SUPABASE_KEY_DATA=..........
```

# Docs
- https://supabase.com/docs/reference/python/auth-signup