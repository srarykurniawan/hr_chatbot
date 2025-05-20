from flask import Flask
from .extensions import db
from .auth import auth_bp
from .admin import admin_bp
from .chatbot import chatbot_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(chatbot_bp)

    return app
