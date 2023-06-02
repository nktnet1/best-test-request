import pytest
from flask import Flask
from flask_app import app as the_app


@pytest.fixture
def app():
    the_app.config.update({"TESTING": True})

    yield the_app

    the_app.config.pop("TESTING")


@pytest.fixture
def client(app: Flask):
    return app.test_client()
