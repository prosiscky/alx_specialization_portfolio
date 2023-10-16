# config.py
# This file configures the database URL as well as SECRET KEY
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///expense.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

