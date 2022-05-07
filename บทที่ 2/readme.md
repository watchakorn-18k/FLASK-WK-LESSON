# บทที่ 2

### 🛑 การใช้ extends
- รูปแบบ
{% extends "a.html" %}


- ภายในไฟล์ a.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    {% block title %}

    {% endblock title %}
</head>

<body>
    {% block content %}

    {% endblock %}
</body>
</html>
```
- เราสามารถระบุ 
block ได้อย่างอิสระ แต่จะต้องมีการปิดด้วย endblock
เช่น 
<br>
    {% block content %}

    {% endblock %}
<br>

content คือชื่อสามารถเปลี่ยนได้

- ตัวอย่างการใช้งานในไฟล์ b.html
```
    {% extends "a.html" %}

    {% block content %}

    <h5>นี่คือบล็อค B</h5>

    {% endblock %}
```

- ตัวอย่างการใช้งานในไฟล์ c.html
```
    {% extends "a.html" %}

    {% block content %}

    <h5>นี่คือบล็อค C</h5>

    {% endblock %}
```