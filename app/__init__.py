from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# Define Flask App
app = Flask(__name__)
#app.config.from_object(app.config)
basedir = os.path.abspath(os.path.dirname(__file__))
# App config
# URI to SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'property_management_db.sqlite')
# Define db access
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Add endpoints
from app.controllers.user_endpoints import mod
from app.controllers.property_endpoints import prop

app.register_blueprint(mod)
app.register_blueprint(prop)

# Build data base
db.create_all()
