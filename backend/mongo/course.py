from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

course = Blueprint('course', __name__)

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
            code = c['code']
            name = c['name']
            credit = c['credit']
            course = {'code': code, 'name': name, 'credit': credit}
            courses.append(course)
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
        return jsonify(subsets)