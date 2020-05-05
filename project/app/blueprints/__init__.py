"""
entry to register all the blueprints
"""
from . import auth
from . import shop
def init_app(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(shop.bp)