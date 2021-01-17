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
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    location = db.Column('location', Geometry('POINT'))
    messages = relationship("Messages")

    def __init__(self, id, location, name):
        self.id = id
        self.name = name
        self.location = location
    def to_json(self):
        print([s.to_json() for s in self.messages])
        return {
            "id":self.id,
            "name": self.name,
            "messages": [s.to_json() for s in self.messages]
        }

class Messages(db.Model):
    __tablename__='messages'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, ForeignKey('users.user_id'))
    content = db.Column('content', db.String)
    timestamp = db.Column('timestamp', db.DateTime)

    def __init__(self, parent_id, content, timestamp):
        self.parent_id = parent_id
        self.content = content
        self.timestamp = timestamp

    def to_json(self):
        return {
            "user": run_transaction(sessionmaker, lambda s: s.query(User).filter_by(id=self.parent_id).first().name),
            "message": self.content,
            "timeSent": self.timestamp
        }

# INSERT INTO messages VALUES (1, 1, 'test', TIMESTAMP '2016-01-25 10:10:10.555');
#  CREATE TABLE messages (id UUID NOT NULL DEFAULT gen_random_uuid(), parent_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE, content STRING, timestamp TIMESTAMP);