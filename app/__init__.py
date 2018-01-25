from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from config import DevelopmentConfig



# Define Flask App
app = Flask(__name__)
# Get config in config file
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Add endpoints
from app.controllers.user_endpoints import mod
from app.controllers.property_endpoints import prop

app.register_blueprint(mod)
app.register_blueprint(prop)

# Build data base
db.create_all()
