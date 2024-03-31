from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                set_access_cookies, set_refresh_cookies, 
                                jwt_required, get_jwt_identity, unset_jwt_cookies)
from mongo import db
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.get_json()
        mail = user.get('email')
        password = user.get('password')
        collection = db["user"]
        u = collection.find_one({"email": mail})
        if u:
            check = u['password']
            if password == check:
                access_token = create_access_token(identity=mail)
                refresh_token = create_refresh_token(identity=mail)
                #response = jsonify()
                #set_access_cookies(response, access_token)
                #set_refresh_cookies(response, refresh_token)
                #print(access_token)
                return jsonify(access_token=access_token), 200
        
    else:
            return jsonify({'error': 'error'})

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
        role = 1
        collection = db["user"]
        collection.insert_one({
            "email" : mail,
            "user_name" : name,
            "password" : password,
            "role" : role,
            "school" : school,
            "department" : department,
            "datetime" : dt
        })
        response_object['message'] = 'success.'
        return jsonify(response_object)
    return

@auth.route('/userinfo', methods = ['GET'])
@jwt_required()
def userinfo():
    print('success')
    email = get_jwt_identity()
    collection = db["user"]
    user = collection.find_one({"email": email})
    name = user['name']
    university = user['school']
    major = user['department']
    if(user['role'] == 1):
        role = '學生'
    else:
        role = '管理者'
    user_data = {'name': name, 'email': email, 'university': university, 'major': major, 'iden': role}
    return jsonify(user_data)