#!/usr/bin/python3
"""5. Number template - module"""
from flask import Flask, render_template

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


@hello.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """is_a_number - function"""
    return '{} is a number'.format(str(n))


@hello.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """num_template - function"""
    return render_template('5-number.html', number=n)


@hello.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """even_odd - function"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n, even_odd='even')
    else:
        return render_template('6-number_odd_or_even.html', number=n, even_odd='odd')


hello.run(debug=True, host='0.0.0.0', port=5000)
