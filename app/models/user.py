from app import db

# USER model
class User(db.Model):
    
    # id (Integer)
    id = db.Column(db.Integer, primary_key=True)
    # User firstname (limited to 120 chars) - Required
    firstname = db.Column(db.String(120), unique=False,nullable= False)
    # User lastname (limited to 120 chars) - Required
    lastname = db.Column(db.String(120), unique=False,nullable= False)
    # User birthday (Date time) - Required
    birthday = db.Column(db.DateTime,unique=False, nullable= False)
    # Email must be unique - Required - Unique
    email = db.Column(db.String(120))
    
    # User Constructor
    def __init__(self, firstname, lastname,birthday,email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.email = email
        