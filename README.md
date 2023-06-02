# Best Test Request

Figuring out the most efficient method to send requests to test web servers

## Usage

1. Install Python dependencies with `poetry install`
2. Install JS dependencies with `npm install`
3. Run the test script with `poetry run python runner.py`

You can use `--progress` to get a live counter (so you know it hasn't broken)

You can also customise the particular variations that are run by editing
`runner.py`.

## List of variations

### Flask

Run server using `poetry run python -m flask_app`

All combinations of:

#### Request strategy

* `requests` library to send requests
* `flask.testing` library to send fake requests

#### Request method

* `GET` with query string
* `POST` with JSON

#### JSON encoder

* Flask's `jsonify` function
* Standard `json` library

### Express

Run server using `npm start`

All combinations of:

#### Request strategy

* `sync-request` to send requests
* Node's built-in `fetch` to send requests

#### Request method

* `GET` with query string
* `POST` with JSON
