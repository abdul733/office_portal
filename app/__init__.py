from flask import Flask
from app.database import Database

database = Database()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    database.init_app(app)

    # register blueprints here later
    return app
