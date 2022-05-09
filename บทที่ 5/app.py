from flask import Flask,render_template,url_for

app = Flask(__name__,static_url_path='/static')

@app.route("/")
def หน้าแรก():
    ข้อมูลผู้ใช้ = [{
        'ชื่อ':'สมชาย สมหญิง',
        'อายุ':'20',
        'สถานะ':'นักเรียน'
    },
    {
        'ชื่อ':'สมหญิง สบายดี',
        'อายุ':'21',
        'สถานะ':'นักเรียน'
    },
    {
        'ชื่อ':'สมสมัย ใจเสมอ',
        'อายุ':'22',
        'สถานะ':'นักเรียน'
    },
    {
        'ชื่อ':'ใจเสมอ สบายดี',
        'อายุ':'23',
        'สถานะ':'นักเรียน'
    },
    {
        'ชื่อ':'สบายดี สมหญิง',
        'อายุ':'24',
        'สถานะ':'นักเรียน'
    }]
    return render_template("index.html",
    data=ข้อมูลผู้ใช้)

@app.route("/เนื้อหา")
def เนื้อหา():
    return render_template("content.html")

@app.route("/ติดต่อ")
def ติดต่อ():
    return render_template("contact.html")

@app.route("/เกี่ยวกับ")
def เกี่ยวกับ():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True,port=10100,host="0.0.0.0",use_reloader=True)
