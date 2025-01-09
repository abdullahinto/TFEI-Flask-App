# This module provides utility functions for the Flask web application.
# It includes functions for file validation, image preprocessing, and text extraction using OCR.

import os
from PIL import Image, ImageFilter
import pytesseract
from pytesseract import TesseractError

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def preprocess_image(image):
    """Preprocess the image for better OCR results."""
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)  # Resize image
    return image

def extract_text_from_image(image_path):
    """Extract text from an image using pytesseract."""
    try:
        image = Image.open(image_path)
        image = preprocess_image(image)
        config = '--oem 3 --psm 6'  # Example config: OCR Engine Mode 3, Page Segmentation Mode 6
        text = pytesseract.image_to_string(image, config=config)
        return text
    except TesseractError as te:
        return f"Error extracting text using Tesseract: {te}"
    except Exception as e:
        return f"Error processing image: {e}"

