#!/usr/bin/python3
"""
Create a new view for Amenities objects
that handles all default RESTFul API actions
"""
from flask import jsonify
from flask import abort
from flask import request
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views


@app_views.route("/amenities", strict_slashes=False)
def get_all_amenities():
    """A route that returns get all amenities"""
    amenity_list = []
    for key, value in storage.all(Amenity).items():
        amenity_list.append(value.to_dict())
        return jsonify(amenity_list)


@app_views.route("/amenities/<amenity_id>", strict_slashes=False)
def get_amenity(amenity_id):
    """A route that returns get amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        return abort(404)


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"], strict_slashes=False)
def delete_amenity(amenity_id):
    """A route that returns delete amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def create_amenity():
    """A route that returns create amenity"""
    if request.content_type != "application/json":
        return abort(400, "Not a JSON")
    if not request.get_json():
        return abort(400, "Not a JSON")
    data = request.get_json()

    if "name" not in data:
        return abort(400, "Missing name")

    amenity = Amenity(**data)

    amenity.save()

    return jsonify(amenity.to_dict()), 200


@app_views.route("/amenities/<amenity_id>", methods=["PUT"], strict_slashes=False)
def update_amenity():
    """A route that returns update amenity"""
    if request.content_type != "application/json":
        return abort(400, "Not a JSON")
    if not request.get_json():
        return abort(400, "Not a JSON")
    data = request.get_json()

    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        ignore_keys = ["id", "created_at", "updated_at"]
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(amenity, key, value)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    else:
        return abort(404)
