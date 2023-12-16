from flask import Blueprint, render_template

about_routes = Blueprint('about', __name__)

@about_routes.route('/about')
def about():
    return render_template('about.html')