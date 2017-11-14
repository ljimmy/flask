"""exceptions"""
from flask import json
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type

class AppException(HTTPException):
    """exception"""
    code = 400
    error = "invalid request"

    def __init__(self, code=None, error=None, description=None, response=None):
        if code is not None:
            self.code = code
            self.error = ""
        if error is not None:
            self.error = error
        super().__init__(description, response)

    def get_body(self, environ=None):

        return text_type(json.dumps(
            dict(
                error=self.error,
                message=self.description
            )
        ))

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

class Unauthorized(AppException):
    """HTTP 401 ERROR"""
    code = 401
    error = "Unauthorized"
    description = "Authorization is required"

class BadRequest(AppException):
    """HTTP 400 ERROR"""
    code = 400
    error = "Bad Request"

    def __init__(self, message=None):
        super().__init__(description=message)


class NotFound(AppException):
    """HTTP 404 ERROR"""
    code = 404
    error = "Not Found"

class ServerError(AppException):
    """HTTP 500 ERROR"""
    code = 500
    error = "Internal Server Error"

    def __init__(self, message=None):
        super().__init__(description=message)
