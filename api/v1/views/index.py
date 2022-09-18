#!/usr/bin/python3
"""Index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel,
           "City": City, "Place": Place, "Review": Review,
           "State": State, "User": User}


@app_views.route("/status")
def api_return():
    """Method that returns the status of the json file"""
    return jsonify({'status': 'OK'})


@app_views.route("/stats", strict_slashes=False)
def objects_count():
    """retrieves the number of each objects by type"""
    response = {}
    PLURALS = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    for key, value in PLURALS.items():
        response[value] = storage.count(key)
    return jsonify(response)
