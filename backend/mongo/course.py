from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

course = Blueprint('course', __name__)

@course.route('/useraddcourse', methods = ['POST'])
@jwt_required()
def user_add_course():
    if request.method == "POST":
        course = request.get_json()
        code = course.get()
        print(code)
        #collection = db['course']
        #c = collection.find_one({'code': code})
        #if c:
        email = get_jwt_identity()
        collection = db['user']
        user = collection.find_one({"email": email})
        clist = user['courses']
        clist.append(code)
        user['courses'] = clist

@course.route('/addcourse', methods = ['POST'])
def add_course():
    if request.method == 'POST':
        course = request.get_json()
        area = course.get('area')
        reqired = course.get('required')
        program = course.get('program')
        name = course.get('name')
        code = course.get('code')
        credit = course.get('credit')
        colletion = db['course']
        
@course.route('/addprogram', methods = ['POST'])
def add_program():
    if request.method == "POST":
        print("test")
        program = request.get_json()
        area = program.get('area')
        name = program.get('name')
        collection = db["program"]
        collection.insert_one({
            "area": area,
            "name": name
        })
    return jsonify({'success': 'success'})