from flask import Flask,render_template,url_for,request,redirect
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
        with sqlite3.connect(db_local) as conn:
            cursor = conn.cursor()
            cursor.execute(f"insert into ListStudent (First_Last,Age,Status) values ('{first_last}',{age},'{status}')")
            conn.commit()

        return redirect(url_for("หน้าแรก"))
    else:
        return render_template("add.html")

@app.route("/ลบรายชื่อ", methods=['GET','POST'])
def delete_record():
    delete_param = request.args.get('delete')
    with sqlite3.connect(db_local) as conn:
            cursor = conn.cursor()
            cursor.execute(f'delete from ListStudent where id = "{delete_param}"')
            conn.commit()
    return redirect(url_for("หน้าแรก"))

@app.route("/แก้ไขรายชื่อ", methods=['GET','POST'])
def update_record():
    if request.method == 'POST':
        first_last = request.form.get("First_Last")
        age = request.form.get("Age")
        status = request.form.get("Status")
        update_param = request.args.get('update')
        with sqlite3.connect(db_local) as conn:
            cursor = conn.cursor()
            cursor.execute(f"update ListStudent set First_Last = '{first_last}',Age = '{age}',Status = '{status}' where id = '{update_param}'")
            conn.commit()

        return redirect(url_for("หน้าแรก"))
    else:
        update_param = request.args.get('update')
        with sqlite3.connect(db_local) as conn:
            cursor = conn.cursor()
            cursor.execute(f"select * from ListStudent where id = '{update_param}'")
            datas = cursor.fetchall()
            return render_template("edit.html",data=datas)


def main():
    app.run(debug=True,port=10100,host="0.0.0.0",use_reloader=True)

if __name__ == "__main__":
    main()
