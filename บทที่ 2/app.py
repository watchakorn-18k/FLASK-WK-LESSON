from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/word")
def word():
    return render_template("word.html")

if __name__ == "__main__":
    app.run(debug=True,port=10100,host="0.0.0.0",use_reloader=True)
