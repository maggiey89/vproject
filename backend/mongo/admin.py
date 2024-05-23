from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

admin = Blueprint('admin', __name__)

@admin.route('/addcourse', methods = ['POST'])
def add_course():
    if request.method == 'POST':
        course = request.get_json()
        name = course.get('name')
        code = course.get('code')
        credit = course.get('credit')
        colletion = db['course']
        c = colletion.find_one({"code" : code})
        if c:
            return jsonify(error = '課程已存在。')
        c = colletion.find_one({'name' : name})
        if c:
            return jsonify(error = '課程已存在。')
        colletion.insert_one({
            "code": code,
            "name": name,
            "credit": credit,
        })
        return jsonify(success = 'success')

@admin.route('/addprogram', methods = ['POST'])
def add_program():
    if request.method == "POST":
        program = request.get_json()
        field = program.get('field')
        courses = program.get('courses')
        name = program.get('name')
        codes = []
        for c in courses:
            codes.append(c['code'])
        collection = db["program"]
        collection.insert_one({
            "field": field,
            "name": name,
            "courses": codes,
        })
    return jsonify(success = 'success')

@admin.route('/addfield', methods = ['POST'])
def add_field():
    if request.method == "POST":
        field = request.get_json()
        name = field.get('name')
        collection = db["field"]
        collection.insert_one({
            "name": name
        })
    return jsonify(success = 'success')

@admin.route('/addsubset', methods = ['POST'])
def add_subset():
    if request.method == 'POST':
        subset = request.get_json()
        field = subset.get('field')
        program = subset.get('program')
        name = subset.get('name')
        courses = subset.get('course')
        credit = subset.get('credit')
        '''
        collection = db["subset"]
        collection.insert_one({
            "field": field,
            "program": program,
            "name": name,
            "courses": courses,
            "credit": credit,
        })
        '''
        return jsonify(success = 'success')