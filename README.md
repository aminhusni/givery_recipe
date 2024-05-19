# Recipe Website API
## Project Stack
This project is written in Python and using the following framework:
- Python 3.10
- Pipenv (pipfile)
- Flask
- SQLAlchemy
- Flask Migration

## Initalization
### Setup the virtual environment
`pipenv install`
### Activate the virtual environment
`pipenv shell`
### Initalize the database
The default initalization code will use the sqlite engine and the DB file will be located in the root directory of the project. 

`flask --app main db upgrade`
### Run the Flask server in development mode
In this development mode, we will run on port 8080 instead of setting up a full server stack such as uWSGI and Nginx. 

`flask --app main run --host=0.0.0.0 --port=8080`