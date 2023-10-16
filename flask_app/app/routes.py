# app/routes.py

from flask import render_template
from app import app, db
from app.models import Expense

@app.route('/')
def add():
    """ renders the home page of the application"""
    return render_template('add.html')
