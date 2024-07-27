from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required,
)
from flask_bcrypt import Bcrypt
from .models import FormLoginUsers, FormResgisterUsers, Users, db
from .models import ContentData, ContentLesson, FormStudent, ListStudent


api = Blueprint("main", __name__)
bcrypt = Bcrypt()


@api.route("/")
def home():
    query_data = ListStudent.query.all()
    return render_template("index.html", data=query_data)


@api.route("/content")
def content():
    query_data = ContentLesson.query.all()
    return render_template("content.html", data={"content_data": query_data})


@api.route("/content/<int:id>")
def content_id(id):
    query_data = ContentData.query.filter_by(lesson_id=id).all()
    return render_template("content-lesson.html", data={"lesson": query_data})


@api.route("/contact")
def contact():
    return render_template("contact.html")


@api.route("/about")
def about():
    return render_template("about.html")


@api.route("/add_student", methods=["GET", "POST"])
@login_required
def add_student():
    if not current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = FormStudent()
    if form.validate_on_submit():
        first_last = form.First_Last.data
        age = form.Age.data
        status = form.Status.data
        add_student = ListStudent(First_Last=first_last, Age=age, Status=status)
        db.session.add(add_student)
        db.session.commit()
        return redirect(url_for("main.home"))

    return render_template("add.html", form=form)


@api.route("/delete_record", methods=["GET", "POST"])
def delete_record():
    id_student = request.args.get("delete")
    delete_student = ListStudent.query.get(id_student)
    db.session.delete(delete_student)
    db.session.commit()
    return redirect(url_for("main.home"))


@api.route("/update_record", methods=["GET", "POST"])
def update_record():
    form = FormStudent()
    if form.validate_on_submit():
        first_last = form.First_Last.data
        age = form.Age.data
        status = form.Status.data
        update_param = request.args.get("update")
        update_student = ListStudent.query.get(update_param)
        update_student.First_Last = first_last
        update_student.Age = age
        update_student.Status = status
        db.session.commit()
        return redirect(url_for("main.home"))

    update_param = request.args.get("update")
    update_student = ListStudent.query.get(update_param)
    return render_template("edit.html", data=update_student, form=form)


@api.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = FormResgisterUsers()
    if form.validate_on_submit():
        password_for_hash = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = Users(
            username=form.username.data,
            password=password_for_hash,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("sign_up.html", form=form)


@api.route("/login", methods=["GET", "POST"])
def login():
    form = FormLoginUsers()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.home"))

    return render_template("login.html", form=form)


@api.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
