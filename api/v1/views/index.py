#!/usr/bin/python3
"""Index file"""

import api.v1.views
from flask import jsonify


@api.v1.views.app_views.route("/status")
def api_return():
    """Method that returns the status of the json file"""
    return jsonify({"status": "OK"})
