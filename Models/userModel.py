from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import *

app= Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    location = db.Column(db.String)
    messages = relationship("Message")

    def __init__(self, location):
        self.location = location

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column('message_id', db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, ForeignKey('users.user_id'))
    content = db.Column(db.String)

    def __init__(self, content):
        self.content = content