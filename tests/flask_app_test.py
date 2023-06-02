"""
Tests for the flask app
"""
import os
import requests
import pytest
from flask.testing import FlaskClient

NUM_ITERATIONS = 1000

REAL_REQUEST = os.getenv("REAL_REQUEST")
GET_REQUEST = os.getenv("GET_REQUEST")


if REAL_REQUEST:
    if GET_REQUEST:
        @pytest.mark.parametrize(
            "input",
            range(NUM_ITERATIONS),
        )
        def test_request_get(input: int):
            response = requests.get(
                "http://127.0.0.1:5001/",
                params={"input": input},
            )
            assert response.json()["output"] == input * 2
    else:
        @pytest.mark.parametrize(
            "input",
            range(NUM_ITERATIONS),
        )
        def test_request_post(input: int):
            response = requests.post(
                "http://127.0.0.1:5001/",
                json={"input": input},
            )
            assert response.json()["output"] == input * 2
else:
    if GET_REQUEST:
        @pytest.mark.parametrize(
            "input",
            range(NUM_ITERATIONS),
        )
        def test_fake_get(client: FlaskClient, input: int):
            response = client.get(
                "/",
                query_string={"input": input},
            )
            assert response.get_json(force=True)["output"] == input * 2
    else:
        @pytest.mark.parametrize(
            "input",
            range(NUM_ITERATIONS),
        )
        def test_fake_post(client: FlaskClient, input: int):
            response = client.post(
                "/",
                json={"input": input},
            )
            assert response.get_json(force=True)["output"] == input * 2
