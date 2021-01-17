from flask import *
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import *
from sqlalchemy.orm import relationship
from sqlalchemy import *
from sqlalchemy.dialects import postgresql
from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy.orm import *
import sqlalchemy.orm

app= Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)


class User(db.Model):
    __tablename__ = 'shrinjay_users'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    location = db.Column('location', Geometry('POINT'))
    messages = relationship("Messages")

    def __init__(self, user_id, location, name):
        self.id = user_id
        self.name = name
        self.location = location
    def to_json(self):
        return {
            "id":self.id,
            "name": self.name,
            "messages": [s.to_json() for s in self.messages]
        }

class Messages(db.Model):
    __tablename__='shrinjay_messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    parent_id = db.Column(db.Integer, ForeignKey('shrinjay_users.id'))
    content = db.Column('content', db.String)
    timestamp = db.Column('timestamp', db.DateTime)

    def __init__(self, parent_id, content, timestamp, name):
        self.parent_id = parent_id
        self.content = content
        self.timestamp = timestamp
        self.name = name

    def to_json(self):
        return {
            "user": self.name,
            "message": self.content,
            "timeSent": self.timestamp
        }
# CREATE TABLE shrinjay_messages(id UUID NOT NULL DEFAULT gen_random_uuid(), parent_id INTEGER REFERENCES shrinjay_users(id), content STRING, timestamp TIMESTAMP, name STRING);

class Session(db.Model):
    __tablename__='shrinjay_session'
    id = db.Column(db.Integer, primary_key=true)
    session_token = db.Column('session_token', db.String)
    location = db.Column('location', Geometry('POINT'))

    def __init__(self, id, session_token, location):
        self.id = id
        self.session_token = session_token
        self.location = location

# INSERT INTO messages VALUES (1, 1, 'test', TIMESTAMP '2016-01-25 10:10:10.555');
#  CREATE TABLE messages (id UUID NOT NULL DEFAULT gen_random_uuid(), parent_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE, content STRING, timestamp TIMESTAMP);