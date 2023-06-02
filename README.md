# Best Test Request

Figuring out the most efficient way to send requests to test web servers

## List of methods

### Flask

All combinations of:

* Request type:
  * `requests` library to send requests (environment variable `REAL_REQUEST`)
  * `flask.testing` library to send fake requests
* Request method:
  * `GET` with query string (environment variable `GET_REQUEST`)
  * `POST` with JSON
* JSON encoder
  * Standard `json` library
  * Flask's `jsonify` function
