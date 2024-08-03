import os


class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
