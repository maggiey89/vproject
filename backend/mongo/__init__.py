from flask import Flask
import pymongo
from pymongo import MongoClient
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)
app.config["SECRET_KEY"] = "490db5992f28fa9f572613d6d53f61e7d15b391b"
app.config["JWT_SECRET_KEY"] = "74df6a1e89ca4ad077ab2b0ed7076b2a808f8000e6fad4f6f5bb44eaed8c8d19"
client = MongoClient("mongodb+srv://emily911008:emily450150@testing.mnvj9qd.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]
jwt.init_app(app)

from .school import school
from .auth import auth

app.register_blueprint(school, url_prefix = '/')
app.register_blueprint(auth, url_prefix = '/')