#!/usr/bin/python3
"""8. List of states - module"""
from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def list_cities_states(id=None):
    """list_cities_states - function"""
    states = []
    cities = []
    for key, value in storage.all(State).items():
        states.append(value)
    for key, value in storage.all(City).items():
        cities.append(value)
    return render_template(
        '9-states.html', states=states, cities=cities, id=id)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """teardown_appcontext - function"""
    storage.close()


app.run(debug=True, host='0.0.0.0', port=5000)
