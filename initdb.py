# Author: Amin Husni
# Date Written: 18 May 2024
# Desc: This is to initialize the database. Please choose the DB engine and conncetion in model.py

from flask import Flask
from sqlalchemy.inspection import inspect

from model import create_DB_instance
from datetime import datetime

app, db, Recipe = create_DB_instance()

with app.app_context():
    if not inspect(db.engine).has_table('recipes'):
        print("Creating database... ")

        db.create_all()

        print("Database created!")

        # Convert into a supported datetime format
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

    else:
        print("Database already exists. Skipping code execution.")
