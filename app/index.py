"""index"""
from flask import jsonify,render_template
from app.libs.routes import route
from app.libs.cache import redis

@route('/')
def index():
    """首页"""
    redis.set('a', 1)
    return jsonify({'index': "首页"})
