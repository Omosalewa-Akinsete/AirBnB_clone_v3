#!/usr/bin/python3
"""Create a flask app that starts an API"""
from flask import jsonify
from api.v1.views import app_views


# Create a route /status on the object app_views that returns JSON
@app_views.route("/status")
def api_status():
    """A route that returns status OK"""
    response = {"status": "OK"}
    return jsonify(response)
