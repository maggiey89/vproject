from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "490db5992f28fa9f572613d6d53f61e7d15b391b"
client = MongoClient("mongodb+srv://emily911008:emily450150@testing.mnvj9qd.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]

from .school import school
from .auth import auth

app.register_blueprint(school, url_prefix = '/')
app.register_blueprint(auth, url_prefix = '/')