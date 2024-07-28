# บทที่ 14  การอัปโหลดรูปภาพจากเว็บขึ้นไปใน AWS S3


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

## Install requirements
```
pip install -r requirements.txt
```

## Start server
```
set FLASK_RUN=run.py
flask run
```

## .env
```.env
SQLALCHEMY_DATABASE_URI = "postgresql://postgres.x................"
AWS_ACCESS_KEY = ...........
AWS_SECRET_KEY = ..........
BUCKET_NAME = .......
```

## Run Dokcer , Podman
```
podman build -t name_images
podman run -it --rm -p 5000:5000 name_images
```