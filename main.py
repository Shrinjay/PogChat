from flask import *
from flask_sqlalchemy import SQLAlchemy
from cockroachdb.sqlalchemy import run_transaction
import sqlalchemy.orm
from Models.userModel import User, Message

# Define endpoint routes and begin implementing:
# For now lets define a get route to get all messages for a certain location
# And a post route to add messages to the DB.
# DB schema will be as discussed, hold userid, messages join and coordinates.
# Send and recieve as JSONs, client side will convert into message objects

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

@app.route('/')
def show_all():
    return run_transaction(sessionmaker, lambda s: jsonify(s.query(User).all()))

app.run()