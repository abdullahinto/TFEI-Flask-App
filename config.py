# This module contains the configuration settings for the Flask web application.
# It includes settings for the secret key, MongoDB URI, and allowed file extensions.

from pymongo import MongoClient

class Config:
    SECRET_KEY = 'supersecretkey'
    MONGO_URI = 'mongodb+srv://newtesting:dbfortesting285@cluster0.crh19.mongodb.net/' 
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}