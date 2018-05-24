#!/usr/bin/python

import sys
sys.path.append("/home/bhaskar/public_html/py/wsgi-bin")
from api import app as application

from flask import Flask

## If uncommented, api.py is not executed
# app = Flask(__name__)

# @app.route('/')
# def hello():
#   return "Hello, Flask"

# if __name__=="__main__":
#   app.run()
