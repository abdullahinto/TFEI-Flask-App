<<<<<<< HEAD
=======
# This module handles interactions with MongoDB, including saving images to GridFS.
# It establishes a connection to the MongoDB database and provides utility functions
# for storing and retrieving files.

>>>>>>> bd45cca (initial commit)
from pymongo import MongoClient
from gridfs import GridFS
from config import Config
from datetime import datetime, timedelta
from bson.objectid import ObjectId


client = MongoClient(Config.MONGO_URI)
db = client.get_database("ocr_db")
fs = GridFS(db)

def save_image_to_mongo(file, filename, ttl_hours=24):
    """
    Save an image file to MongoDB GridFS with an expiry timestamp.
    """
    expire_at = datetime.utcnow() + timedelta(hours=ttl_hours)
    file_id = fs.put(file, filename=filename, metadata={"expireAt": expire_at})
    return file_id

def retrieve_image_from_mongo(file_id):
    """Retrieve an image file from MongoDB GridFS."""
    return fs.get(file_id)
