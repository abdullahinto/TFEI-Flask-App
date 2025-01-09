<<<<<<< HEAD
=======
# This module defines the routes for the Flask web application.
# It includes the main route for rendering the index page and a route for handling file uploads.
# The routes are configured and attached to the Flask app instance.

>>>>>>> bd45cca (initial commit)
from flask import render_template, request, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
from utils import allowed_file, extract_text_from_image
from config import Config
from mongo_utils import save_image_to_mongo

def configure_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)

            file = request.files['file']
            if file.filename == '':
                flash('No selected file. Just Upload and Click "Extract" to see the MAGIC!✨')
                return redirect(request.url)

            if file and allowed_file(file.filename, Config.ALLOWED_EXTENSIONS):
                filename = secure_filename(file.filename)
                
                # Save file to MongoDB
                file_id = save_image_to_mongo(file, filename)

                # Process the file for text extraction
                extracted_text = extract_text_from_image(file)
                flash('File successfully uploaded and text extracted.')
                return render_template('index.html', extracted_text=extracted_text)
            else:
                flash('⚠️Invalid file format. Please upload a PNG, JPG, or JPEG file.')
                return redirect(request.url)
        else:
            return redirect('/')

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
