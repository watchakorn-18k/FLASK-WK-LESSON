from flask import Flask
from app.main.routes import api
from app.main.routes import bcrypt
from app.main.models import Users, db
from flask_login import LoginManager


def web_app():
    app = Flask(__name__, static_url_path="/static")
    login_manager = LoginManager()

    # Load configuration
    app.config.from_object("app.config.Config")
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def loader_user(user_id):
        return Users.query.get(user_id)

    # Register Blueprints
    app.register_blueprint(api)

    return app
