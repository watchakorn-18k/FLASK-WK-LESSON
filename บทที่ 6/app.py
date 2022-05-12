from flask import Flask,render_template,url_for,request
import sqlite3
db_local = 'DB.db'
app = Flask(__name__,static_url_path='/static')

@app.route("/")
def หน้าแรก():
    connect = sqlite3.connect(db_local)
    cursor = connect.cursor()
    cursor.execute("select * from ListStudent")
    ข้อมูลผู้ใช้ = cursor.fetchall()
    return render_template("index.html",data=ข้อมูลผู้ใช้)

@app.route("/เนื้อหา")
def เนื้อหา():
    return render_template("content.html")

@app.route("/ติดต่อ")
def ติดต่อ():
    return render_template("contact.html")

@app.route("/เกี่ยวกับ")
def เกี่ยวกับ():
    return render_template("about.html")

@app.route("/เพิ่มนักเรียน" , methods=['GET','POST'])
def เพิ่มนักเรียน():
    if request.method == 'POST':
        first_last = request.form.get("First_Last")
        age = request.form.get("Age")
        status = request.form.get("Status")
        connect = sqlite3.connect(db_local)
        cursor = connect.cursor()
        cursor.execute(f"insert into ListStudent (First_Last,Age,Status) values ('{first_last}',{age},'{status}')")
        connect.commit()
        connect.close()
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True,port=10100,host="0.0.0.0",use_reloader=True)
