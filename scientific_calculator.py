import imp
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

#Run server
@app.route('/')
def index():
    return 'Simple Flask Alchemist API'

if __name__ == '__main__':
    app.run(debug=True)



