#!/usr/bin/python3
"""0. Hello Flask! -  module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """hello_flask - function"""
    return 'Hello HBNB!'


app.run(debug=True, host='0.0.0.0', port=5000)
