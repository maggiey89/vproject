from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

course = Blueprint('course', __name__)

@course.route('/useraddcourse', methods = ['POST'])
@jwt_required()
def user_add_course():
    if request.method == "POST":
        course = request.get_json()
        code = course.get('course')
        collection = db['course']
        c = collection.find_one({'code': code})
        if c:
            email = get_jwt_identity()
            collection = db['user']
            collection.update_one({"email": email}, {"$push": {"courses": code}})
            return jsonify({'success': 'success'})
        else:
            return jsonify(error = '學分學程中無此課程。')
    
@course.route('/usercourses', methods = ['GET'])
@jwt_required()
def get_user_courses():
    email = get_jwt_identity()
    collection = db['user']
    user = collection.find_one({"email": email})
    if user:
        return jsonify({'courses': user['courses']})

@course.route('/getfield', methods = ['GET'])
def all_field():
    if request.method == 'GET':
        fields = []
        collection = db['field']
        for f in collection.find():
            field = f['name']
            fields.append(field)
        return jsonify(fields)
    
@course.route('/getprogram', methods = ['POST'])
def getProgram():
    if request.method == 'POST':
        f = request.get_data(as_text=True)
        programs = []
        collection = db['program']
        for p in collection.find({'field': f}):
            program = p['name']
            programs.append(program)
        return jsonify(programs)
    
@course.route('/getcourse', methods = ['POST', 'GET'])
def get_course():
    if request.method == 'POST':
        p = request.get_json()
        program = p['program']
        courses = []
        collection = db['course']
        for c in collection.find({'program': program}):
            c['_id'] = ''
            courses.append(c)
        return jsonify(courses)
    else:
        courses = []
        collection = db['course']
        for c in collection.find():
            c['_id'] = ''
            courses.append(c)
        return jsonify(courses)
