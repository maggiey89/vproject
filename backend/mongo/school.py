from flask import Blueprint, request, jsonify
from mongo import db

school = Blueprint('school', __name__)

@school.route('/school', methods = ['GET', 'POST'])
def all_school():
    if request.method == 'GET':
        schools = []
        collection = db['school']
        for s in collection.find():
            s['_id'] = ''
            schools.append(s)
        return jsonify(schools)
