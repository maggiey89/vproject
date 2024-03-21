from flask import Blueprint, request, jsonify, flash, session
from flask_cors import CORS
from mongo import db
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        response_object = {'status':'success'}
        user = request.get_json()
        mail = user.get('email')
        password = user.get('password')
        collection = db["user"]
        user = collection.find_one({"email": mail})
        if user:
            check = user['password']
            if password == check:
                session["email"] = mail
                response_object['message'] = 'success.'
                return jsonify(response_object)

@auth.route('/signup', methods = ["GET", 'POST'])
def sign_up():
    if request.method == "POST":
        response_object = {'status':'success'}
        new_user = request.get_json()
        mail = new_user.get('email')
        name = new_user.get('name')
        password = new_user.get('password')
        school = new_user.get('school')
        department = new_user.get('department')
        dt = datetime.now()
        collection = db["user"]
        collection.insert_one({
            "email" : mail,
            "user_name" : name,
            "password" : password,
            "school" : school,
            "department" : department,
            "datetime" : dt
        })
        response_object['message'] = 'success.'
        return jsonify(response_object)
    return