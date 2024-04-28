#!/usr/bin/python3
"""Create a flask app that starts an API"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views)

# Run the Flask server
if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    PORT = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=HOST, port=PORT, threaded=True)
