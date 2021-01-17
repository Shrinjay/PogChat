from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)



