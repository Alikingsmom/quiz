from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# import vsex funksii
from database.leadersservice import *
from database.questionservice import *
from database.registerservice import *
