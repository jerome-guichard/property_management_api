# property_management_api
Property Management API

API to CRUD users and properties

## Environment setup:
1- Install required packages:
First of all, install virtualenv 
virtualenv is a tool to create isolated Python environments
```
$pip install virtualenv
```
Go into the app package and:
```
$ cd property_management_api
$ virtualenv venv
```
Activate the env by running the script 'activate':
```
$ venv\Script\activate
```

Then install all the required packages, they will only be installed into the python virtual env
```
$pip install flask
$pip install flask_sqlalchemy
$pip install flask_marshmallow
$pip install marshmallow-sqlalchemy
$pip install unidecode
```

## App setup:

1-In console into the app package: 
$python run.py

It sets up the API and the SQLite DB

2- Test in your browser:
```
http://localhost:5000/api/users
``` 
```
http://localhost:5000/api/properties
```
You should not get any error message.

## Test

To go through the following steps, you need a rest client test tool like Advanced Rest Client.

### Users

Get all users in DB:
```
GET http://localhost:5000/api/users/
```

Get a specific user in DB:
```
GET http://localhost:5000/api/users/<userId>
```

Create a user in DB:
```
POST http://localhost:5000/api/users
```
with json body: (all the fields are required)
```
{
  "lastname":"Jackson",
  "firstname":"Michael",
  "birthday":"1958-08-29",
  "email":"ja@mi.fr"
}
```

Update a user information DB:
```
PUT http://localhost:5000/api/users/<userId>
```
with json body: (one field is sufficient)
```
{
  "lastname":"Jackson",
  "firstname":"Michael Joseph",
  "birthday":"1958-08-29",
  "email":"ja@mi.fr"
}
```

Delete a user in DB:
```
DELETE http://localhost:5000/api/users/<userId>
```

### PROPERTIES

Get all properties in DB:
```
GET http://localhost:5000/api/properties/
```

Get a specific property in DB:
```
GET http://localhost:5000/api/users/<propertyId>
```

Get a all properties located in a specific city in DB:
```
GET http://localhost:5000/api/users/<cityName>
```


Create a property in DB:
```
POST http://localhost:5000/api/properties
```
with json body: (all the fields are required)
```
{
  "name":"Elysee",
  "description":"Quartier sûr, Proche commerces",
  "city":"Paris",
  "room":"1",
  "owner_id":"1"
}
```

Update a property information DB:
```
PUT http://localhost:5000/api/properties/<propertyId>
```
with json body: (one field is sufficient)
```
{
  "room":"365",
}
```

Delete a property in DB:
```
DELETE http://localhost:5000/api/properties/<userId>
```

