from app import db

# PROPERTY Model in DB
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