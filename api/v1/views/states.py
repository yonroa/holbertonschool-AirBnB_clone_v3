#!/usr/bin/python3
"""Update states"""

from os import abort
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify

@app_views.route("/states")
def get_state():
    """Method for state"""
    new_list = []
    for state in storage.all("State").values():
        new_list.append(state.to_dict())
    return jsonify(new_list)


@app_views.route("/states/<string:state_id>")
def one_state(state_id):
    """Method for one state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

