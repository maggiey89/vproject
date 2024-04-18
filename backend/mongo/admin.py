from flask import Blueprint, request, jsonify
from mongo import db
from flask_jwt_extended import jwt_required, get_jwt_identity

admin = Blueprint('admin', __name__)

@admin.route('/addcourse', methods = ['POST'])
def add_course():
    if request.method == 'POST':
        course = request.get_json()
        field = course.get('field')
        required = course.get('type')
        program = course.get('program')
        name = course.get('name')
        code = course.get('code')
        credit = course.get('credit')
        colletion = db['course']
        if required == '必修':
            required = 1
        else:
            required = 0
        colletion.insert_one({
            "field": field,
            "program": program,
            "code": code,
            "name": name,
            "type": required,
            "credit": credit,
        })
        return jsonify({'success': 'success'})

@admin.route('/addprogram', methods = ['POST'])
def add_program():
    if request.method == "POST":
        program = request.get_json()
        field = program.get('field')
        name = program.get('name')
        collection = db["program"]
        collection.insert_one({
            "field": field,
            "name": name
        })
    return jsonify({'success': 'success'})

@admin.route('/addfield', methods = ['POST'])
def add_field():
    if request.method == "POST":
        print("test")
        field = request.get_json()
        name = field.get('name')
        collection = db["field"]
        collection.insert_one({
            "name": name
        })
    return jsonify({'success': 'success'})