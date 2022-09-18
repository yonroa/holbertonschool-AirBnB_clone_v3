#!/usr/bin/python3
"""Update states"""

from flask import abort, request, jsonify, make_response
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False)
def get_state():
    """Method for state"""
    new_list = []
    for state in storage.all("State").values():
        new_list.append(state.to_dict())
    return jsonify(new_list)


@app_views.route("/states/<string:state_id>", strict_slashes=False)
def one_state(state_id):
    """Method for one state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<string:state_id>", methods=["DELETE"],
                 strict_slashes=False)
def state_delete(state_id):
    """Method that deletes a state object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify(({})), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_post():
    """Method that creates a state"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if "name" not in data:
        abort(400, description="Missing name")
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route("/states/<string:state_id>", methods=['PUT'],
                 strict_slashes=False)
def state_put(state_id):
    """Method that puts a state"""
    state = storage.get("State", state_id)
    data = request.get_json()
    if not state:
        abort(404)
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
        storage.save()
        return make_response(jsonify(state.to_dict()), 200)
