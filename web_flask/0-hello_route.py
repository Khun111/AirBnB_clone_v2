#!/usr/bin/python3
'''Module for a script that starts a Flask web application'''
from flask import Flask
myapp = Flask(__name__)

@myapp.route('/', strict_slashes=False)
def greet():
    '''Run on route'''
    return 'Hello HBNB!'

if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port=5000)
