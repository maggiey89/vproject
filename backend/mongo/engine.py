from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from mongoengine import *
import mongoengine
from mongo import db

class User(Document):
    class Role():
        ADMIN = 0
        STUDENT = 1
    
    name = StringField(max_length=20, required = True)
    email = EmailField(required = True)
    role = IntField(default = Role.STUDENT)
    school = StringField(max_length = 16, default = '')
    password = StringField(max_length = 12)
    department = StringField(max_length = 16, default = '')
    courses = ListField(default = [])
    '''
    collection = db['user']
    @classmethod
    def singup(self, ):
    '''
    
    
        
class School(FlaskForm):
    abbr = StringField(max_length = 16, required = True)
    name = StringField(max_length = 256)