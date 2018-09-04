from flask import Flask
from flask_bootstrap import Bootstrap

from views import blue

def create_app():
    app = Flask(__name__)
    app.secret_key = '123456'
    app.register_blueprint(blueprint=blue)
    Bootstrap(app)
    return app