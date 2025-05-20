from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Import & register blueprint
    from .export.routes import export_bp
    from .auth.routes import auth_bp
    from .dashboard.routes import dashboard_bp
    from .chatbot.routes import chatbot_bp

    app.register_blueprint(export_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(chatbot_bp)

    return app
