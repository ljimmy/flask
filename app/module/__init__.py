from .main import bp as main_blueprint
from .api import register_api_blueprint

def register_blueprint(app):
    app.register_blueprint(main_blueprint)
    register_api_blueprint(app)
