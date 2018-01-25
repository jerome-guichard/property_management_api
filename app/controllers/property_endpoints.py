# Import DB from app
from app import db
# Import user model
from app.models.property import Property
# Import User schema
from sqlalchemy.exc import IntegrityError
from app.schemas.property_schema import PropertySchema
from flask import Blueprint, request, jsonify
import unidecode as ud 
import json


prop = Blueprint('prop', __name__)

# Instancies of user schema
property_schema = PropertySchema()           # Single user
properties_schema = PropertySchema(many=True) # Multiple user

# PROPERTIES ENDPOINT

@prop.route("/api/properties", methods=["POST"])
def add_property():
    
    # Make sure the json is correct otherwise return 400
    # If not a json
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message":"This is not a proper json"}),400 
    
    # Validate and deserialize property
    data, errors = property_schema.load(json_data)
    if errors:
        return jsonify(errors),422 
    
    # Check presence of keys
    if 'name' not in json_data:
        return jsonify({"message":"name missing!"}),400
    if 'description' not in json_data:
        return jsonify({"message":"description missing!"}),400
    if 'city' not in json_data:
        return jsonify({"message":"city missing!"}),400
    if 'room' not in json_data:
        return jsonify({"message":"room missing!"}),400
    if 'owner_id' not in json_data:
        return jsonify({"message":"owner_id missing!"}),400
    
    # Create new Property in base
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    room = request.json['room']
    owner_id = request.json['owner_id']
    
    # Create new instance of Property
    new_property = Property(name, description, city, room, owner_id)

    db.session.add(new_property)
    db.session.commit()

    return property_schema.jsonify(new_property)


# endpoint to show all users
@prop.route("/api/properties", methods=["GET"])
def get_properties():
    all_properties = Property.query.all()
    result = properties_schema.dump(all_properties)
    
    return properties_schema.jsonify(all_properties)


# endpoint to get user detail by id
@prop.route("/api/properties/<int:property_id>", methods=["GET"])
def user_detail(property_id):
    try:    
        # Get details of a specific User
        user = Property.query.get(property_id)
    except IntegrityError:
        return jsonify({"message":"User could not be found"}),400
    
    #Protect result
    if user is None:
        return jsonify({"message":"User could not be found"}),400
    # return user
    return property_schema.jsonify(user)

# endpoint filter by city
@prop.route("/api/properties/<city>", methods=["GET"])
def property_by_city(city):
    
    try:
        # Get All properties located in the city given in URL
        # Lower param and remove accent to match with the model
        all_properties = Property.query.filter_by(city=ud.unidecode(city.lower())).all()
    except IntegrityError:
        return jsonify({"message":"Property could not be found"}),400
    
    result = properties_schema.dump(all_properties)
    
    return jsonify({"Properties in "+city:result.data})

# endpoint to update property
@prop.route("/api/properties/<int:property_id>", methods=["PUT"])
def property_update(property_id):
    
    # GET Porperty  by id
    try:
        property = Property.query.get(property_id)
    except IntegrityError:
        return jsonify({"message":"Property could not be found"}),404
        # Return message if no user found
    if property is None:
        return jsonify({"message":"Property could not be found"}),404
    
    # Check JSON validity 
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message":"This is not a proper json"}),400 
    
    # Update only present keys
    if 'name' in json_data:
        name = json_data['name']
        property.name = name 
    if 'description' in json_data:
        description = json_data['description']
        property.description = description
    if 'city'in json_data:
        city = json_data['city']
        property.city = city 
    if 'room' in json_data:
        room = json_data['room']
        property.room = room 
    if 'owner_id' in json_data:
        owner_id = json_data['owner_id']
        property.owner_id = owner_id
    
    db.session.commit()
    return property_schema.jsonify(property)

# Debug facilty
# endpoint to delete property
@prop.route("/api/properties/<int:property_id>", methods=["DELETE"])
def property_delete(property_id):
    
    # Get Property by id
    try:
        property = Property.query.get(property_id)
    except IntegrityError:
        return jsonify({"message":"Property could not be found"}),404
    # Return message if no user found
    if property is None:
        return jsonify({"message":"Property could not be found"}),404
    
    db.session.delete(property)
    db.session.commit()

    return property_schema.jsonify(property)
