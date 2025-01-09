# This is the main entry point for the Flask web application.
# It initializes the Flask app, loads the configuration, and sets up the routes.
# Finally, it runs the app in debug mode if the script is executed directly.

from flask import Flask
from config import Config
from routes import configure_routes

app = Flask(__name__)
app.config.from_object(Config)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
