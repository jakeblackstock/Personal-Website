from flask import Blueprint, render_template

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def home():
    user_name = "Jake"
    return render_template('index.html', user_name=user_name)
