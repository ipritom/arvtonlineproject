from flask import Flask
from .admin.routes import admin
from .general.routes import site
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    #reginstering admin and site to the blue print
    app.register_blueprint(admin)
    app.register_blueprint(site)

    #set a secret key
    app.config['SECRET_KEY'] = 'secretkey'

    #connecting MongoDB
    app.config['MONGO_URI'] ="mongodb+srv://arvtonline:6ST3HjBqEBc77bd@cluster0.roavi.mongodb.net/arvtdb?retryWrites=true&w=majority"
    mongo.init_app(app)
    
    return app