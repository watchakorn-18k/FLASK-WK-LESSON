# บทที่ 13 การใช้ AWS S3 ในการเก็บไฟล์รูปภาพเบื้องต้น


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
SQLALCHEMY_DATABASE_URI = ""postgresql://postgres.x................"
```

## Run Dokcer , Podman
```
podman build -t name_images
podman run -it --rm -p 5000:5000 name_images
```