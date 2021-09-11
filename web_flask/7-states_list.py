#!/usr/bin/python3
"""8. List of states - module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """list_states - function"""
    states = []
    for key, value in storage.all(State).items():
        states.append(value)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """teardown_appcontext - function"""
    storage.close()


app.run(debug=True, host='0.0.0.0', port=5000)
