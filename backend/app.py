from flask import Flask
from flask_cors import CORS
from mongo import app

app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origines':'*'}}, supports_credentials= True)

@app.route('/', methods = ['GET'])
def home():
    return ('HelloWorld.')

@app.route('/test', methods = ['GET'])
def test():
    return ('test page.')

if __name__ == '__main__':
    app.run(debug = True) 
