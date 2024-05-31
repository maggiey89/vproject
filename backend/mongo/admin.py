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
        collection = db["subset"]
        collection.insert_one({
            "field": field,
            "program": program,
            "name": name,
            "courses": courses,
            "credit": credit,
        })
        return jsonify(success = 'success')
    
@admin.route('/deletecourse', methods = ['POST'])
def delete_course():
    if request.method == 'POST':
        code = request.get_data(as_text=True)
        collection = db['course']
        collection.delete_one({'code': code})
        collection1 = db['program']
        for p in collection1.find():
            courses = p['courses']
            if code in courses:
                print(code)
                courses.remove(code)
                collection1.update_one({'_id': p['_id']}, {'$set': {'courses': courses}})
        collection1 = db['subset']
        for s in collection1.find():
            courses = s['courses']
            if code in courses:
                print(code)
                courses.remove(code)
                collection1.update_one({'_id': s['_id']}, {'$set': {'courses': courses}})
        return jsonify(success = 'success')
    
@admin.route('/editcourse', methods = ['POST'])
def edit_course():
    if request.method == 'POST':
        editcourse = request.get_json()
        ocode = editcourse['ocode']
        ncode = editcourse['ncode']
        nname = editcourse['nname']
        credit = editcourse['credit']
        collection = db['course']
        collection.update_one({'code': ocode}, {'$set': {'code': ncode, 'name': nname, 'credit': credit}})

