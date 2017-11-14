def register_api_blueprint(app):
    from .api_1_0 import bp as api_v1
    app.register_blueprint(api_v1)
