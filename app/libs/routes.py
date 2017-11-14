"""routes"""
from .error import ServerError
class Routes(object):
    """app routes"""
    _app = None

    @classmethod
    def add(cls, rule, **options):
        """add rule"""
        if cls._app is None:
            raise ServerError("not set app")
        def decorator(func):
            """decorator"""
            endpoint = options.pop('endpoint', None)
            cls._app.add_url_rule(rule, endpoint, func, **options)
            return func
        return decorator

    @classmethod
    def init_app(cls, app):
        """init route app"""
        cls._app = app

route = Routes.add
