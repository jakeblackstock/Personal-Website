# from app import app
from flask import Blueprint

home_routes = Blueprint('home_routes', __name__)

# Define a route within the blueprint
@home_routes.route('/')
def home():
    return 'Hello Jake'
