#!/usr/bin/python3
"""3. Python is cool! -  module"""
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


@hello.route('/python', strict_slashes=False)
@hello.route('/python/', strict_slashes=False)
@hello.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """hello_python - function"""
    return 'Python {}'.format(text.replace('_', ' '))


hello.run(debug=True, host='0.0.0.0', port=5000)
