# Best Test Request

Figuring out the most efficient method to send requests to test web servers

## Usage

1. Install Python dependencies with `poetry install`
2. Install JS dependencies with `npm install`
3. Run the test script with `poetry run python runner.py`

You can use `--progress` to get a live counter (so you know it hasn't broken)

# List of methods

## Flask

Run server using `poetry run python -m flask_app`

All combinations of:

#### Request strategy

* `requests` library to send requests (environment variable `REAL_REQUEST`)
* `flask.testing` library to send fake requests

#### Request method

* `GET` with query string (environment variable `GET_REQUEST`)
* `POST` with JSON

#### JSON encoder

* Flask's `jsonify` function (environment variable `FLASK_JSONIFY`)
* Standard `json` library

## Express

Run server using `npm start`

All combinations of:

#### Request strategy

* `sync-request` to send requests (environment variable `SYNC_REQUEST`)
* Node's built-in `fetch` to send requests

#### Request method

* `GET` with query string (environment variable `GET_REQUEST`)
* `POST` with JSON
