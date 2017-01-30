import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgres://pfhuoxshwdihhf:981ecaa3cb0ac95c658610b7122a8a08e80a64d1bb7a1bac0f9b3f739166b7e3@ec2-54-235-247-224.compute-1.amazonaws.com:5432/ddq4e8054n9hok"
    DEBUG = True
    SECRET_KEY = os.environ.get("TEXTBOOK_SECRET_KEY", os.urandom(12))