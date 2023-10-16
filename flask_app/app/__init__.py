# app/__init__.py
# Initializations for the app

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask-migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

