#!/usr/bin/python3
"""9. Cities by states - module"""
from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_states():
    """list_cities_states - function"""
    states = []
    cities = []
    for key, value in storage.all(State).items():
        states.append(value)
    for key, value in storage.all(City).items():
        cities.append(value)
    return render_template('8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """teardown_appcontext - function"""
    storage.close()


app.run(debug=True, host='0.0.0.0', port=5000)
