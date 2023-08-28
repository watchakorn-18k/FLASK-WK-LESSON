from flask import Flask,render_template,url_for,request,redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Length
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
app = Flask(__name__,static_url_path='/static')
login_manager = LoginManager()
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///School.db"
app.config['SECRET_KEY'] = bcrypt.generate_password_hash('wk18k').decode('utf-8')

db.init_app(app)
login_manager.init_app(app)

class ListStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_Last = db.Column(db.String(250))
    Age = db.Column(db.Integer)
    Status = db.Column(db.String(50))

class FormStudent(FlaskForm):
    First_Last = StringField('first_last', validators=[DataRequired()])
    Age = IntegerField('age', validators=[DataRequired()])
    Status = StringField('status', validators=[DataRequired()])
    Submit = SubmitField('submit')

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    permission_admin = db.Column(db.Boolean, default=False)

class FormResgisterUsers(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(8,20, message='รหัสผ่านต้องมีความยาว 8-20 ตัวอักษร')])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password', message='รหัสผ่านไม่ตรงกัน')])
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    permission_admin = BooleanField('permission_admin', default=False)
    submit_register = SubmitField('submit')

class FormLoginUsers(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(8,20, message='รหัสผ่านต้องมีความยาว 8-20 ตัวอักษร')])
    submit_login = SubmitField('submit')

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route("/")
def home():
    query_data = ListStudent.query.all()
    return render_template("index.html",data=query_data)

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
    form = FormStudent()
    if form.validate_on_submit():
        first_last = form.First_Last.data
        age = form.Age.data
        status = form.Status.data
        add_student = ListStudent(First_Last=first_last,Age=age,Status=status)
        db.session.add(add_student)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("add.html",form=form)

@app.route("/ลบรายชื่อ", methods=['GET','POST'])
def delete_record():
    id_student = request.args.get('delete')
    delete_student = ListStudent.query.get(id_student)
    db.session.delete(delete_student)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/แก้ไขรายชื่อ", methods=['GET','POST'])
def update_record():
    form = FormStudent()
    if form.validate_on_submit():
        first_last = form.First_Last.data
        age = form.Age.data
        status = form.Status.data
        update_param = request.args.get('update')
        update_student = ListStudent.query.get(update_param)
        update_student.First_Last = first_last
        update_student.Age = age
        update_student.Status = status
        db.session.commit()
        return redirect(url_for("home"))
    
    update_param = request.args.get('update')
    update_student = ListStudent.query.get(update_param)
    return render_template("edit.html",data=update_student,form=form)


@app.route('/สมัครสมาชิก', methods=["GET", "POST"])
def register():
    form = FormResgisterUsers()
    
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if form.validate_on_submit():
        password_for_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data,
                     password=password_for_hash,first_name=form.first_name.data,last_name=form.last_name.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html",form=form)

@app.route("/เข้าสู่ระบบ", methods=["GET", "POST"])
def login():
    form = FormLoginUsers()
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("home"))  
    
    return render_template("login.html",form=form)

@app.route("/ออกจากระบบ")
def logout():
    logout_user()
    return redirect(url_for("home"))


def main():
    app.run(debug=True,port=10100,host="0.0.0.0",use_reloader=True)

if __name__ == "__main__":
    main()
