# บทที่ 4

### 🛑 การใช้ static
#### คำสั่ง
```
app = Flask(__name__, static_url_path='/static')
```
```cs
static_url_path='/static'
```
- static_url_path คือการบอก Flask ว่าตำแหน่งโฟลเดอร์ของ static อยู่ที่ไหน
- '/static' คือชื่อของโฟลเดอร์ที่เก็บไฟล์ static ของเว็บไซต์

<a href="https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask#answer-26554578">อ้างอิงจาก sharpshadow</a>

#### การใช้งาน
- ตัวอย่างเช่นเราจะระบุให้ไฟล์ css เข้าไปทำงานใน html สามารถใช้
```
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
```
- จากวิดีโอเราได้สร้างไฟล์ style.css ไว้ใน static/css แล้ว
