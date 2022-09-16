#!/usr/bin/python3
"""Index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {"Amenity": 'Amenity', "BaseModel": 'BaseModel', "City": 'City',
           "Place": 'Place', "Review": 'Review', "State": 'State', "User": 'User'}


@app_views.route("/status")
def api_return():
    """Method that returns the status of the json file"""
    return jsonify({'status': 'OK'})

@app_views.route("/stats")
def objects_count():
    """retrieves the number of each objects by type"""
    new_dict = {}
    for k, v in classes.items():
        new_dict[k] = storage.count(v)
    return new_dict
