# Best Test Request

Figuring out the most efficient method to send requests to test web servers.

## Context

I've been experimenting with various ways to try and speed up COMP1531's test
runners, and also check how the performance of various other request-related
things relate.

## Findings

Here's a [link to the results](https://github.com/MiguelGuthridge/best-test-request/actions/runs/5155195155).

* Using sync-request is about 5x slower than using the fetch API.
* Python is about twice as slow as JS when sending real requests.
* When injecting fake requests using Flask's testing library (instead of
  sending real requests), performance improves by 5x.
* If we can find a library to inject fake requests into Express, we may be able
  to get a similar performance improvement, meaning the improvement would be
  25x compared to using sync-request.

## Usage

Here's how you can run the benchmarks on your own machine.

Note: I'm using Poetry as the dependency management tool for Python. You'll
need to [install it](https://python-poetry.org/docs/).

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
