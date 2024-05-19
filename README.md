# Recipe Website API
## Project Stack
This project is written in Python and uses the following framework:
- Python 3.10
- Pipenv (pipfile)
- Flask
- SQLAlchemy
- Flask Migration

A sample of API test cases is given in the Postman Collection JSON file.<br>
Instructions on how to run the code will be at the end of this Readme. 

## Author's Comment
Even though this is a test project, I am using all of the frameworks and ORM engine that I would normally use in a project. This practice is done so that such projects can be scaled or expanded in the future as needed. <br><br>
uWSGI and Nginx are not used for the sake of simplicity and also, that is what I usually do for projects that are
still under development and are not fully deployed. <br><br>
HTTPS/TLS will also be ignored in this test as it is not a specified requirement. <br><br>
Postman API platform software is used, is what I normally use to keep track of my development, testing and later to be converted into the API documentation. 

## Hidden Cases or Unspecified Specifications
In this project, there are some outputs or behaviours that are not strictly specified. These are solved with some assumptions and with the REST Architechtural Constrains in mind. 

| Case       | Solution      |
| ------------- | ------------- |
| 500 Errors| Provided own message in JSON.|
| 405 Error (wrong method) | Will be converted into 404 error as <br> the test requires all endpoints other than stated should be 404.|
| Long `GET /recipes` result| Pagination can be implemented if needed. <br>Since the given expected response is defined,<br> pagination information cannot be implemented here.  |
| `/recipes/{id}` is not interger| Return 404 error with invalid API path message. |
| Partial parameter in `PATCH /recipes/{id}`| Unspecified if all parameters are required. <br> This code will accept partial parameters and <br> only update the supplied parameters.  |
| `GET /recipes/{id}` with optional parameter| The other option parameters are `created_at` and <br> `updated_at`. This code will accept query parameter: <br> `/recipes/{id}?created_at=True&updated_at=True` <br> to enable showing the optional parameters.  |
| `POST /recipes` failure reponse message | Failure response message is showing all the required <br> parameters. However, this test does not specify if <br> this is a static error message or showing the missing <br> parameters. <br> This code will check which parameter is missing <br> and show which required parameter was missing. |


## Initialization
### Setup the virtual environment
`pipenv install`
### Activate the virtual environment
`pipenv shell`
### Initalize the database
The default initialization code will use the sqlite engine and the DB file will be located in the root directory of the project. 

`flask --app main db upgrade`
### Run the Flask server in development mode
In this development mode, we will run on port 8080 instead of setting up a full server stack such as uWSGI and Nginx. 

`flask --app main run --host=0.0.0.0 --port=8080`