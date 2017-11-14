from functools import wraps

from flask import Blueprint, request

from app.libs.cache import redis
from app.libs.error import Unauthorized
from app.models.user import Session


bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
route = bp.route

def api(rule, **options):
    def decorator(view, pk='id', pk_type='int'):
        view_func = view.as_view(view.__name__)
        bp.add_url_rule(rule, defaults={pk: None},
                        view_func=view_func, methods=['GET',])
        bp.add_url_rule(rule, view_func=view_func, methods=['POST',])
        bp.add_url_rule('%s<%s:%s>' % (rule, pk_type, pk), view_func=view_func,
                        methods=['GET', 'PUT', 'DELETE'])
        return view
    return decorator

def auth(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Access-Token', None)
        if not token:
            raise Unauthorized()
        uid = int(redis.hget('user_token',token))
        if not uid:
            raise Unauthorized()
        if not Session.setUid(uid):
            raise Unauthorized()
        Session.token = token
        return f(*args, **kwargs)
    return decorator

from . import passport
from . import user