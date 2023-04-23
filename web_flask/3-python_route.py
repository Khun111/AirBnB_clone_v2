#!/usr/bin/python3
'''Module for a script that starts a Flask web application'''
from flask import Flask
myapp = Flask(__name__)


@myapp.route('/', strict_slashes=False)
def greet():
    '''Run on route'''
    return 'Hello HBNB!'


@myapp.route('/hbnb', strict_slashes=False)
def display():
    '''Run on route'''
    return 'HBNB'


@myapp.route('/c/<text>', strict_slashes=False)
def handlevars(text):
    '''Run on route'''
    text = text.replace('_', ' ')
    return f'C {text}'


@myapp.route('/python/<text>', strict_slashes=False)
@myapp.route('/python/', strict_slashes=False)
def pyvars(text='is_cool'):
    '''Run on route'''
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port=5000)
