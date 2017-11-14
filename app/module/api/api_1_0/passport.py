"""登录注册
"""
from flask.views import MethodView
from flask import request, jsonify
from app.libs.error import BadRequest
from app.models import serialize
from app.models.user import (
    login as user_login,
    join as user_join,
)
from . import route


def generate_token(uid):
    from uuid import uuid1
    from app.libs.cache import redis
    token = str(uuid1()).replace('-', '')
    redis.hset('user_token', token, uid)
    return token

@route('/passport/login', methods=['POST'])
def login():
    """登录
    """
    mobile = request.form.get('mobile', None)
    password = request.form.get('password', None)
    user = user_login(mobile, password)
    if not user:
        raise BadRequest("无效的账户名或密码")
    return jsonify({'token': generate_token(user.id)})

@route("/passport/join", methods=['POST'])
def join():
    """注册
    """
    mobile = request.form.get('mobile', None)
    password = request.form.get('password', None)
    user = user_join(mobile, password)

    if not user:
        raise BadRequest("已存在")
    return jsonify({'token': generate_token(user.id)})
