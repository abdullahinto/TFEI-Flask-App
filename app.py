<<<<<<< HEAD
=======
# This is the main entry point for the Flask web application.
# It initializes the Flask app, loads the configuration, and sets up the routes.
# Finally, it runs the app in debug mode if the script is executed directly.

>>>>>>> bd45cca (initial commit)
from flask import Flask
from config import Config
from routes import configure_routes

app = Flask(__name__)
app.config.from_object(Config)

configure_routes(app)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True) 
=======
    app.run(debug=True)
>>>>>>> bd45cca (initial commit)
