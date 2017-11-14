from werkzeug.local import LocalProxy
from flask import g,current_app
def init_app(app):
    from redis import StrictRedis
    app.extensions['redis'] = StrictRedis(**app.config['REDIS'])



def get_redis():
    d = getattr(g, 'redis', None)
    return d or current_app.extensions['redis']


redis = LocalProxy(get_redis)
