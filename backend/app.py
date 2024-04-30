from flask import Flask
from flask_cors import CORS
from mongo import app

app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origines':'*'}}, supports_credentials= True)

if __name__ == '__main__':
    app.run(debug = True) 
 