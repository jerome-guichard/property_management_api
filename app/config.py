import os
_basedir = os.path.abspath(os.path.dirname(__file__))

#DEBUG = True
#TESTING = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'property_management_db.sqlite')

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'property_management_db.sqlite')

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True