from app import db
import unidecode as ud 

# PROPERTY Model in DB
class Property(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Name of the property - Required
    name = db.Column(db.String(255),unique=False,nullable= False)
    # Description - Not Unique - Not Required
    description = db.Column(db.String(255),unique=False,nullable= True)
    # City - Not Unique - Required
    city = db.Column(db.String(255),unique=False,nullable= False)
    # Number of rooms - Not Unique - Required
    room = db.Column(db.Integer,unique=False,nullable= False)
    # ID of the owner
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))  
    # User profile of the owner
    #user = db.relationship("User",
    #                         backref=db.backref("properties", lazy="dynamic"))
    
    # Property constructor
    def __init__(self, name, description, city, room, owner_id):
        self.name = name
        self.description = description
        # Lower "city" str and remove accents to improve query results on that field
        self.city = ud.unidecode(city.lower())
        self.room = room
        self.owner_id = owner_id
