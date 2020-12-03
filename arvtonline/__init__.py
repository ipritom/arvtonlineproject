from flask import Flask
from .admin.routes import admin
from .general.routes import site

def create_app():
    app = Flask(__name__)

    #reginstering admin and site to the blue print
    app.register_blueprint(admin)
    app.register_blueprint(site)

    return app