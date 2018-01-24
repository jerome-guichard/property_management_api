from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Define Flask App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# App config
# URI to SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'property_management_db.sqlite')
# Define db access
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    
    # id (Integer)
    id = db.Column(db.Integer, primary_key=True)
    # User firstname (limited to 80 chars)
    firstname = db.Column(db.String(80), unique=False)
    # User lastname (limited to 80 chars)
    lastname = db.Column(db.String(80), unique=False)
    # User birthday (Date time)
    birthday = db.Column(db.DateTime)
    
    # User Constructor
    def __init__(self, firstname, lastname,birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

# Schema for DB (structure of endpoints responses)
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname', 'lastname','birthday')

# Instancies of user schema
user_schema = UserSchema()           # Single user
users_schema = UserSchema(many=True) # Multiple user

# Property Model in DB
class Property(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Name of the property
    name = db.Column(db.String(80))
    # Description
    description = db.Column(db.String(200))
    # City
    city = db.Column(db.String(200))
    # Number of rooms
    room = db.Column(db.Integer)
    # userid of the owner -> ownerid -> to be linked to User model
    userid = db.Column(db.String(200))
    
    # Property constructor
    def __init__(self, name, description, city, room, userid):
        self.name = name
        self.description = description
        self.city = city
        self.room = room
        self.userid = userid

# Property Schema
class PropertySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'description','city','room','userid')


property_schema = PropertySchema() # Single property
properties_schema = PropertySchema(many=True) # Multiple Porperties


# ENPOINTS

# endpoint to create new user
@app.route("/users", methods=["POST"])
def add_user():
    # Get parameters
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthday = datetime.strptime(request.json['birthday'],'%Y-%m-%d') # Convert str to python date time
    
    # Instantiate new User
    new_user = User(firstname, lastname, birthday)
    
    # Insert in DB
    db.session.add(new_user)
    db.session.commit()
    
    # Return inserted user
    return user_schema.jsonify(new_user)


# endpoint to show all users
@app.route("/users", methods=["GET"])
def get_user():
    # Query all users in DB
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    
    # Return Json containing all the users in DB
    return jsonify(result.data)

# endpoint to get user detail by id
@app.route("/users/<id>", methods=["GET"])
def user_detail(id):
    # Get details of a specific User
    user = User.query.get(id)
    
    # return user
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/users/<id>", methods=["PUT"])
def user_update(id):
    # Get specific user in DB
    user = User.query.get(id)
    
    # Get parameters
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthday = request.json['birthday']
    
    # change User attributes
    user.firstname = firstname
    user.lastname = lastname
    user.birthday = birthday 
    
    # Restore in DB
    db.session.commit()
    
    # Return user
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/users/<id>", methods=["DELETE"])
def user_delete(id):
    # Get user
    user = User.query.get(id)
    # Delete in DB
    db.session.delete(user)
    db.session.commit()
    
    # return user
    return user_schema.jsonify(user)


# PROPERTIES ENDPOINT

@app.route("/properties", methods=["POST"])
def add_property():
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    room = request.json['room']
    userid = request.json['userid']
        
    new_property = Property(name, description, city, room, userid)

    db.session.add(new_property)
    db.session.commit()

    return property_schema.jsonify(new_property)


# endpoint to show all users
@app.route("/properties", methods=["GET"])
def get_properties():
    all_properties = Property.query.all()
    result = properties_schema.dump(all_properties)
    
    return jsonify(result.data)

# endpoint filter by city
@app.route("/properties/<city>", methods=["GET"])
def property_by_city(city):
    # Get All properties located in the city given in URL
    all_properties = Property.query.filter_by(city=city).all()
    result = properties_schema.dump(all_properties)
    
    return jsonify(result.data)


# endpoint to update property
@app.route("/properties/<id>", methods=["PUT"])
def property_update(id):
    property = Property.query.get(id)
    
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    room = request.json['room']
    userid = request.json['userid']

    property.name = name
    property.description = description
    property.city = city 
    property.room = room
    property.userid = userid  

    db.session.commit()
    return property_schema.jsonify(property)


# endpoint to delete property
@app.route("/properties/<id>", methods=["DELETE"])
def property_delete(id):
    property = Property.query.get(id)
    db.session.delete(property)
    db.session.commit()

    return property_schema.jsonify(property)

# Start app
if __name__ == '__main__':
    app.run(debug=True)

