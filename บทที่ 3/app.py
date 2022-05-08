from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def หน้าแรก():
    return render_template("index.html")

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
