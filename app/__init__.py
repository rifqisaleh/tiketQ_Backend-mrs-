from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Import models AFTER extensions are initialized
    from app.models import ticket
    from app.routes.ticket_routes import ticket_bp
    app.register_blueprint(ticket_bp, url_prefix="/tickets")
    
    @app.route("/", methods=["GET"])
    def root():
        return {"message": "Welcome to TicketQ"}


    return app
