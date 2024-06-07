from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

user = Blueprint('user', __name__)

@user.route('/useraddcourse', methods = ['POST'])
@jwt_required()
def user_add_course():
    if request.method == "POST":
        course = request.get_json()
        codes = course.get('course')
        email = get_jwt_identity()
        collection = db['user']
        user = collection.find_one({"email": email})
        for c in codes:
            courses = user['courses']
            if c not in courses:
                collection.update_one({"email": email}, {"$push": {"courses": c}})
        return jsonify(success = 'success')
    
@user.route('/usercourses', methods = ['GET'])
@jwt_required()
def get_user_courses():
    email = get_jwt_identity()
    collection = db['user']
    user = collection.find_one({"email": email})
    if user:
        return jsonify(user['courses'])
    
@user.route('/userdeletecourse', methods = ['POST'])
@jwt_required()
def user_delete_course():
    if request.method == 'POST':
        email = get_jwt_identity()
        collection = db['user']
        course = request.get_json()
        code = course.get('course')
        user = collection.find_one({"email": email})
        courses = user['courses']
        courses.remove(code)
        collection.update_one({'_id': user['_id']}, {'$set': {'courses': courses}})
        return jsonify(success = 'success')
