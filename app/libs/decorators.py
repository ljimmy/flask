"""decorators"""
from functools import wraps
from flask import request
from app.libs.error import Unauthorized

def authenticator(func):
    """authenticator"""
    @wraps(func)
    def decorator(*args, **kwargs):
        """decorator"""
        token = request.headers.get('access_token', None)
        if not token or token is None:
            raise Unauthorized()
        return func(*args, **kwargs)
    return decorator
