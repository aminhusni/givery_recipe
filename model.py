# Author: Amin Husni
# Date Written: 18 May 2024
# Desc: This is where the database ORM model will be defined. Seed data is defined here too.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime

# Database connection

db = SQLAlchemy()

# Recipe SQL Model database


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    making_time = db.Column(db.String(100), nullable=False)
    serves = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Recipe {self.title}>'

    def inital_seed_data():
        # Convert into a supported datetime format
        # These are converted from the original SQL file provided.
        created_at_1 = datetime.strptime(
            '2016-01-10 12:10:12', '%Y-%m-%d %H:%M:%S')
        updated_at_1 = datetime.strptime(
            '2016-01-10 12:10:12', '%Y-%m-%d %H:%M:%S')
        created_at_2 = datetime.strptime(
            '2016-01-11 13:10:12', '%Y-%m-%d %H:%M:%S')
        updated_at_2 = datetime.strptime(
            '2016-01-11 13:10:12', '%Y-%m-%d %H:%M:%S')

        print("Inserting two sample recipes... ")
        # Insert two sample recipe entries
        chicken_curry = Recipe(id=1, title='Chicken Curry', making_time='45 min', serves='4 people',
                               ingredients='onion, chicken, seasoning', cost=1000, created_at=created_at_1, updated_at=updated_at_1)
        rice_omu = Recipe(id=2, title='Rice Omelette', making_time='30 min', serves='2 people',
                          ingredients='onion, egg, seasoning, soy sauce', cost=700, created_at=created_at_2, updated_at=updated_at_2)

        db.session.add(chicken_curry)
        db.session.add(rice_omu)
        db.session.commit()
