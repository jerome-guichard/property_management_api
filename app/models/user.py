from app import db

# USER model
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