# Recipe Website API
## Project Stack
This project is written in Python and using the following framework:
- Python 3.10
- Pipenv (pipfile)
- Flask
- SQLAlchemy
 
## Initalization
### Setup the virtual environment
`pipenv install`
### Activate the virtual environment
`pipenv shell`
### Initalize the database
The default initalization code will use the sqlite engine and the DB file will be located in the root directory of the project. 

`python initdb.py`
### Run the Flask server in development mode
In this development mode, it will run on port 8080

`python main.py`