from app import db
import unidecode as ud 

# PROPERTY Model in DB
class Property(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Name of the property
    name = db.Column(db.String(255))
    # Description
    description = db.Column(db.String(255))
    # City
    city = db.Column(db.String(255))
    # Number of rooms
    room = db.Column(db.Integer)
    # userid of the owner -> ownerid -> to be linked to User model
    userid = db.Column(db.String(255))
    
    # Property constructor
    def __init__(self, name, description, city, room, userid):
        self.name = name
        self.description = description
        # Lower "city" str and remove accents to improve query results on that field
        self.city = ud.unidecode(city.lower())
        self.room = room
        self.userid = userid