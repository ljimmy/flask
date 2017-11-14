"""init app"""
from flask import Flask
from config import CONFIG_FILE

def register_base(app):

    from .models import db
    db.init_app(app)

    from .libs import cache
    cache.init_app(app)
    
    from app.libs.routes import Routes
    Routes.init_app(app)

def register_error(app):
    from .libs.error import NotFound

    @app.errorhandler(404)
    def handle_not_found(e):
        return NotFound()

def import_view():
    """import view"""
    from . import index

def create_app(config_name):
    """create app"""

    app = Flask(__name__)
    app.config.from_pyfile(CONFIG_FILE[config_name])
    #register base
    register_base(app)
    #register error
    register_error(app)
    #register view
    import_view()
    # register blueprint
    from .module import register_blueprint
    register_blueprint(app)

    return app