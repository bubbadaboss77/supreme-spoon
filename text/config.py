import os

class DevelopmentConfig(object):
    DATABASE_URL = "postgres://pfhuoxshwdihhf:981ecaa3cb0ac95c658610b7122a8a08e80a64d1bb7a1bac0f9b3f739166b7e3@ec2-54-235-247-224.compute-1.amazonaws.com:5432/ddq4e8054n9hok"
    DEBUG = True
    SECRET_KEY = os.environ.get("TEXTBOOK_SECRET_KEY", os.urandom(12))

#new and obtained from heroku documentation    
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)    