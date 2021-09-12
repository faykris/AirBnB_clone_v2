#!/usr/bin/python3
"""8. List of states - module"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State, City
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def list_all_data():
    """list_all_data - function"""
    states = []
    cities = []
    amenities = []
    places = []
    users = []
    for key, value in storage.all(State).items():
        states.append(value)
    for key, value in storage.all(City).items():
        cities.append(value)
    for key, value in storage.all(Amenity).items():
        amenities.append(value)
    for key, value in storage.all(Place).items():
        places.append(value)
    for key, value in storage.all(User).items():
        users.append(value)
    return render_template(
        '100-hbnb.html', states=states,
        cities=cities, amenities=amenities,
        places=places, users=users)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """teardown_appcontext - function"""
    storage.close()


app.run(debug=True, host='0.0.0.0', port=5000)
