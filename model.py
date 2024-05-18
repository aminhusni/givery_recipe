# Author: Amin Husni
# Date Written: 18 May 2024
# Desc: This is where the database type, model (schema) and connection will be defined. 

import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

def create_DB_instance():
    app = Flask(__name__)
    # Database connection
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'recipe.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    # Recipe SQL Model database
    class Recipe(db.Model):
        __tablename__ = 'recipes'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        making_time = db.Column(db.String(100), nullable=False)
        serves = db.Column(db.String(100), nullable=False)
        ingredients = db.Column(db.String(300), nullable=False)
        cost = db.Column(db.Integer, nullable=False)
        created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
        updated_at = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

        def __repr__(self):
            return f'<Recipe {self.title}>'


    return app, db, Recipe