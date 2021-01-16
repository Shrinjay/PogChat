from flask import *
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import *
from sqlalchemy.orm import relationship
from sqlalchemy import *

app= Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    location = db.Column('location', Geometry('POINT'))
    messages = db.Column('messages', db.JSON)

    def __init__(self, location):
        self.location = location
