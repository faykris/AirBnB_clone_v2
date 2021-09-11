#!/usr/bin/python3
"""1. HBNB -  module"""
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


hello.run(debug=True, host='0.0.0.0', port=5000)
