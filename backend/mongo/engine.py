from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from mongoengine import *

class User(FlaskForm):
    class Role():
        ADMIN = 0
        STUDENT = 1
    
    name = StringField(max_length=20, required = True)
    email = EmailField(required = True)
    role = IntField(default = Role.STUDENT)
    

class School(FlaskForm):
    abbr = StringField(max_length = 16, required = True)
    name = StringField(max_length = 256)