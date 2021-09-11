#!/usr/bin/python3
"""2. C is fun! -  module"""
from flask import Flask

hello = Flask(__name__)


@hello.route('/', strict_slashes=False)
def hello_flask():
    """hello_flask - function"""
    return 'Hello HBNB!'


@hello.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """hello_hbnb - function"""
    return 'HBNB'


@hello.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """hello_c - function"""
    return 'C {}'.format(text.replace('_', ' '))


hello.run(debug=True, host='0.0.0.0', port=5000)
