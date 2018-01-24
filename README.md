# property_management_api
Property Management API

Env setup:
1- Install required packages:
	$pip install flask
	$pip install flask_sqlalchemy
	$pip install flask_marshmallow
	$pip install marshmallow-sqlalchemy


App setup:

1- Open a python prompt into the app package
	>>from api.py import db
	>>db.create_all()

It starts the SQLite DB (property_management_db.sqlite)

2- exit the prompt

3- In console: 
	$python api.py

It sets up the API

4- Test in a browser: 
	http://localhost:5000/users
	http://localhost:5000/