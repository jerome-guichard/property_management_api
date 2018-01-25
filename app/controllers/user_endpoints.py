# Import user model
from app.models.user import User
from app.schemas.user_schema import UserSchema
# Import DB from app
from app import db
# Import SQLAlchemy Exception
from sqlalchemy.exc import IntegrityError

from flask import Blueprint, request, jsonify
from datetime import datetime

mod = Blueprint('user', __name__)

# Instancies of user schema
user_schema = UserSchema()           # Single user
users_schema = UserSchema(many=True) # Multiple user

# USER ENPOINTS

# endpoint to create new user
@mod.route("/api/users", methods=["POST"])
def add_user():
    
    # Make sure the json is correct otherwise return 400
    # If not a json
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message":"This is not a proper json"}),400 
    
    # Check presence of keys
    if 'firstname' not in json_data:
        return jsonify({"message":"firstname missing!"}),400
    if 'lastname' not in json_data:
        return jsonify({"message":"lastname missing!"}),400
    if 'birthday' not in json_data:
        return jsonify({"message":"birthday missing!"}),400
    if 'email' not in json_data:
        return jsonify({"message":"email missing!"}),400
    
    # Get keys
    firstname = json_data['firstname']
    lastname = json_data['lastname']
    
    birthday = datetime.strptime(json_data['birthday'],'%Y-%m-%d') # Convert str to python date time
    email = json_data['email']
    
    # Instantiate new User
    new_user = User(firstname, lastname, birthday,email)
    
    # Insert in DB
    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        return jsonify({"message":"User already exists!"}),400
    
    # Return inserted user
    return user_schema.jsonify(new_user)

# endpoint to show all users
@mod.route("/api/users", methods=["GET"])
def get_user():
    
    # Query all users in DB
    all_users = User.query.all()
    
    result = users_schema.dump(all_users)
    
    # Return Json containing all the users in DB
    return jsonify({"Users":result.data})

# endpoint to get user detail by id
@mod.route("/api/users/<int:user_id>", methods=["GET"])
def user_detail(user_id):
    try:    
        # Get details of a specific User
        user = User.query.get(user_id)
    except IntegrityError:
        return jsonify({"message":"User could not be found"}),400
    
    #Protect result
    if user is None:
        return jsonify({"message":"User could not be found"}),400
    # return user
    return user_schema.jsonify(user)


# endpoint to update user
@mod.route("/api/users/<int:user_id>", methods=["PUT"])
def user_update(user_id):
    
    try:
        # Get specific user in DB
        user = User.query.get(user_id)
    except IntegrityError:
        return jsonify({"message":"User could not be found"}),400
    # Return message if no user found
    if user is None:
        return jsonify({"message":"User could not be found"}),400
    
    # Check JSON validity 
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message":"This is not a proper json"}),400 
    
    # Update only present keys
    if 'firstname' in json_data:
        firstname = json_data['firstname']
        user.firstname = firstname 
    if 'lastname' in json_data:
        lastname = json_data['lastname']
        user.lastname = lastname
    if 'birthday'in json_data:
        birthday = datetime.strptime(json_data['birthday'],'%Y-%m-%d')
        user.birthday = birthday
    if 'email' in json_data:
        email = json_data['email']
        user.email = email  
    
    # Restore in DB
    db.session.commit()
    
    # Return user
    return user_schema.jsonify(user)

# endpoint to delete user
@mod.route("/api/users/<int:user_id>", methods=["DELETE"])
def user_delete(user_id):
    
    try:
        # Get user
        user = User.query.get(user_id)
    except IntegrityError:
        return jsonify({"message":"User could not be found"}),400
    # Return message if no user found
    if user is None:
        return jsonify({"message":"User could not be found"}),400
    
    # Delete in DB
    db.session.delete(user)
    db.session.commit()
    
    # return user
    return user_schema.jsonify(user)
