from flask import Flask
from routes.home import home_routes

app = Flask(__name__)

# Register blueprints with the app
app.register_blueprint(home_routes)

if __name__ == '__main__':
    app.run(debug=True)
