#!/usr/bin/python3
"""8. List of states - module"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State, City

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def list_drop_down():
    """drop_down - function"""
    states = []
    cities = []
    amenities = []
    for key, value in storage.all(State).items():
        states.append(value)
    for key, value in storage.all(City).items():
        cities.append(value)
    for key, value in storage.all(Amenity).items():
        amenities.append(value)
    return render_template(
        '10-hbnb_filters.html', states=states,
        cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """teardown_appcontext - function"""
    storage.close()


app.run(debug=True, host='0.0.0.0', port=5000)
