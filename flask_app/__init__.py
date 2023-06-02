"""
A simple flask server
"""
import os
import json
from flask import Flask, request, jsonify


FLASK_JSONIFY = os.getenv('FLASK_JSONIFY') is not None


app = Flask(__name__)


if FLASK_JSONIFY:
    @app.post('/')
    def root_post_jsonify():
        assert request.json is not None
        number: int = request.json["input"]
        return jsonify({"output": number * 2})

    @app.get('/')
    def root_get_jsonify():
        number = int(request.args["input"])
        return jsonify({"output": number * 2})
else:
    @app.post('/')
    def root_post():
        assert request.json is not None
        number: int = request.json["input"]
        return json.dumps({"output": number * 2})

    @app.get('/')
    def root_get():
        number = int(request.args["input"])
        return json.dumps({"output": number * 2})
