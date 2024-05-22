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
        return jsonify(user['courses'])

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
    
def get_course_info(code):
    collection = db['course']
    c = collection.find_one({'code': code})
    course = {'name': c['name'], 'code': c['code'], 'credit': c['credit']}
    return course
    
@course.route('/getcourses', methods = ['POST', 'GET'])
def get_courses():
    if request.method == 'POST':
        program = request.get_data(as_text=True)
        courses = []
        collection = db['program']
        p = collection.find_one({'name': program})
        codes = p['courses']
        for c in codes:
            course = get_course_info(c)
            courses.append(course)
        return jsonify(courses)
    else:
        courses = []
        collection = db['course']
        for c in collection.find():
            c['_id'] = ''
            courses.append(c)
        return jsonify(courses)

@course.route('/getcoursesbycode', methods = ['POST', 'GET'])
def getcourses_by_code():
    if request.method == 'POST':
        code = request.get_json()
        codes = code['code']
        courses = []
        for c in codes:
            course = get_course_info(c)
            courses.append(course)
        return jsonify(courses)
    
@course.route('/getsubset', methods = ['POST'])
def get_subset():
    if request.method == 'POST':
        program = request.get_data(as_text=True)
        subsets = []
        collection = db['subset']
        for s in collection.find({'program': program}):
            subset = {'name': s['name'], 'courses': s['courses'], 'credit': s['credit']}
            subsets.append(subset)
        print(subsets)
        return jsonify(success = 'success')