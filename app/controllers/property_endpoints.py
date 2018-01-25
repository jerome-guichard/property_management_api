# Import DB from app
from app import db
# Import user model
from app.models.property import Property
# Import User schema
from sqlalchemy.exc import IntegrityError
from app.schemas.property_schema import PropertySchema
from flask import Blueprint, request, jsonify
import unidecode as ud 


prop = Blueprint('prop', __name__)

# Instancies of user schema
property_schema = PropertySchema()           # Single user
properties_schema = PropertySchema(many=True) # Multiple user

# PROPERTIES ENDPOINT

@prop.route("/api/properties", methods=["POST"])
def add_property():
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    room = request.json['room']
    userid = request.json['userid']
    
    # Create new instance of Property
    new_property = Property(name, description, city, room, userid)

    db.session.add(new_property)
    db.session.commit()

    return property_schema.jsonify(new_property)


# endpoint to show all users
@prop.route("/api/properties", methods=["GET"])
def get_properties():
    all_properties = Property.query.all()
    result = properties_schema.dump(all_properties)
    
    return jsonify({"Properties":result.data})

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
    
    print(property_id)
    print(request.json['name'])            
    
    name = request.json['name']
    description = request.json['description']
    city = request.json['city']
    room = request.json['room']
    userid = request.json['userid']
    
    try:
        property = Property.query.get(property_id)
    except IntegrityError:
        return jsonify({"message":"Property could not be found"}),404
        # Return message if no user found
    if property is None:
        return jsonify({"message":"Property could not be found"}),404
    
    property.name = name
    property.description = description
    property.city = city 
    property.room = room
    property.userid = userid  

    db.session.commit()
    return property_schema.jsonify(property)


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

