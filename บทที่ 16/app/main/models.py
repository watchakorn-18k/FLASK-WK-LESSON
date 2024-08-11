from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    BooleanField,
    PasswordField,
    FileField,
)

from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class ListStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_Last = db.Column(db.String(250))
    Age = db.Column(db.Integer)
    Status = db.Column(db.String(50))


class ContentLesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_name = db.Column(db.String(250))
    content_detail = db.Column(db.String(250))
    image_url = db.Column(db.String(250))


class ContentData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("content_lesson.id"))
    lesson_name = db.Column(db.String(250))
    lesson_detail = db.Column(db.String(250))


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    permission_admin = db.Column(db.Boolean, default=False)


class FormContent(FlaskForm):
    content_name = StringField("content name", validators=[DataRequired()])
    content_detail = StringField("content detail", validators=[DataRequired()])
    image_file = FileField("image cover")
    Submit = SubmitField("submit")


class FormStudent(FlaskForm):
    First_Last = StringField("first_last", validators=[DataRequired()])
    Age = IntegerField("age", validators=[DataRequired()])
    Status = StringField("status", validators=[DataRequired()])
    Submit = SubmitField("submit")


class FormResgisterUsers(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(8, 20, message="รหัสผ่านต้องมีความยาว 8-20 ตัวอักษร"),
        ],
    )
    confirm_password = PasswordField(
        "confirm_password",
        validators=[DataRequired(), EqualTo("password", message="รหัสผ่านไม่ตรงกัน")],
    )
    first_name = StringField("first_name")
    last_name = StringField("last_name")
    permission_admin = BooleanField("permission_admin", default=False)
    submit_register = SubmitField("submit")


class FormLoginUsers(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(8, 20, message="รหัสผ่านต้องมีความยาว 8-20 ตัวอักษร"),
        ],
    )
    submit_login = SubmitField("submit")
