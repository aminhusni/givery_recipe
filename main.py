# Author: Amin Husni
# Date Written: 18 May 2024

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, got_request_exception
from errors import custom_api_error_handler

from sqlalchemy.sql import func
from sqlalchemy.orm.exc import NoResultFound
from multidict import MultiDict

import os
import json

app = Flask(__name__)
got_request_exception.connect(custom_api_error_handler, app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'recipe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Recipe SQL Model
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

### API STARTS HERE      
#POST /recipes, to create a recipe. #GET /recipes, to get a recipes list. 
@app.route('/recipes', methods=['GET', 'POST'])
def create_recipes(): 

    # GET 
    if request.method == 'GET':
        # Just a simple get request, query from database and return. 
        recipes_list = Recipe.query.all()
        serialized_recipes = [{"id": recipe.id,
                               "title": recipe.title,
                               "making_time": recipe.making_time,
                               "serves": recipe.serves,
                               "ingredients": recipe.ingredients,
                               "cost": recipe.cost}
                              for recipe in recipes_list
        ]

        return {"recipes": serialized_recipes}
    
    # POST
    elif request.method == 'POST':

        received_data = request.get_json()

        # Potential return here
        # First, we check for any missing parameters
        expected_parameters = ['title', 'making_time', 'serves', 'ingredients', 'cost']
        missing_parameters = [param for param in expected_parameters if param not in received_data]

        # Tell the requester which paramter is missing that is required. 
        if missing_parameters:
            return {"message": "Recipe creation failed!", "required": ', '.join(missing_parameters)}
        ## Missing parameter check end. 

        # Make the variable human readable
        title = received_data['title']
        making_time = received_data['making_time']
        serves = received_data['serves']
        ingredients = received_data['ingredients']
        cost = received_data['cost']
        
        # Insert into database
        new_recipe = Recipe(title=title, making_time=making_time, serves=serves, ingredients=ingredients, cost=cost)
        db.session.add(new_recipe)
        db.session.commit()

        # Get reply from database (id, creation time, updated time)
        db.session.refresh(new_recipe)
        id = new_recipe.id
        created_at = new_recipe.created_at
        updated_at = new_recipe.updated_at

        serialized_response = [{
                                "id": new_recipe.id, 
                                "title": new_recipe.title, 
                                "making_time": new_recipe.making_time, 
                                "serves": new_recipe.serves, 
                                "ingredients": new_recipe.ingredients, 
                                "cost": new_recipe.cost, 
                                "created_at": new_recipe.created_at, 
                                "updated_at": new_recipe.updated_at
        }]
        
        return {"message": "Recipe successfully created!", "recipe": serialized_response}


#GET /recipes/{id}, to get a recipe. PATCH to update. DELETE to delete. 
@app.route('/recipes/<rec_id>', methods=['GET', 'PATCH', 'DELETE'])
def indiv_recipes(rec_id):

    # Isolate global parameter (relation to method)
    recipe_id = request.view_args['rec_id']

    # Check if recipe exist first? 
    try:
        recipe_instance = Recipe.query.filter_by(id=recipe_id).one()
    except NoResultFound:
        return {"message": "No recipe found"}, 404

    ### GET with optional parameters
    if request.method == 'GET':
        serialized_recipes = [{
                                "id": recipe_instance.id,
                                "title": recipe_instance.title,
                                "making_time": recipe_instance.making_time,
                                "serves": recipe_instance.serves,
                                "ingredients": recipe_instance.ingredients,
                                "cost": recipe_instance.cost
        }]

        # Optional parameters
        if request.args.get('created_at'):
            serialized_recipes[0]["created_at"] = recipe_instance.created_at
        if request.args.get('updated_at'):
            serialized_recipes[0]["updated_at"] = recipe_instance.updated_at

        return {"message": "Recipe details by id", "recipe": serialized_recipes}
    
    ### PATCH
    elif request.method == 'PATCH':

        received_data = request.get_json()

        # Update only paramters that needed to be updated. 
        update_paramters = [param for param in received_data]
        for param in update_paramters:
            setattr(recipe_instance, param, received_data[param])

        db.session.commit()

        # Reply back the latest DB query status of recipe 
        # so the user can check if it has actually been updated. 
        recipe = Recipe.query.filter_by(id=recipe_id).first()
        serialized_recipes = [{
                            "title": recipe.title,
                            "making_time": recipe.making_time,
                            "serves": recipe.serves,
                            "ingredients": recipe.ingredients,
                            "cost": recipe.cost
        }]

        return {"message": "Recipe sucessfully updated!", "recipe": serialized_recipes}

    ### DELETE
    elif request.method == 'DELETE':

        db.session.delete(recipe_instance)
        db.session.commit()
        return {"message": "Recipe sucessfully removed!"}


@app.route('/')
def hello_world():
    return "Invalid API path", 404


@app.errorhandler(Exception)
def page_not_found(e):
    try:
        if e.code == 405:
            return {"message": "Method not allowed or supported for this API path"}, 405
        if e.code == 404:
            return "Invalid API path", 404
    except:
        return {"message": "Critical Backend Error"}, 500
    
    
app.run(host="0.0.0.0", port=8080, debug=True)
