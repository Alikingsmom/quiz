from flask import Flask
from database import db


app = Flask(__name__)


# settings of data base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
# connect SQLALCHEMY to Flask
db.init_app(app)
