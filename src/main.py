from flask import Flask
from application.configuration.database import get_connection
from repository.user.user_repository import UserRepository
from application.api.user_routes import build_user_routes

def create_app():
    app = Flask(__name__)

    db_conn = get_connection()
    user_repository = UserRepository(db_conn)

    app.register_blueprint(build_user_routes(user_repository))
    
    @app.route("/health")
    def health():
        return {"status": "KyberFin API running 🎯"}

    return app
