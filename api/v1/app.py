#!/usr/bin/python3
"""Api"""

from models import storage
from api.v1.views import app_views
import flask
import os

app = flask.Flask(__name__)


app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def recover_api(self):
    """Method app for api"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return flask.make_response(flask.jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
