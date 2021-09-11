#!/usr/bin/python3
"""0. Hello Flask! -  module"""
from flask import Flask

hello = Flask(__name__)


@hello.route('/', strict_slashes=False)
def hello_flask():
    """hello_flask - function"""
    return 'Hello HBNB!'


hello.run(debug=True, host='0.0.0.0', port=5000)
