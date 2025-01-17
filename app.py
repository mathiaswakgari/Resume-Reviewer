import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import docx
from PyPDF2 import PdfReader
import spacy


app = Flask(__name__)

# Upload Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# NLP model
nlp = spacy.load("en_core_web_sm")

os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

def allowed_file(filename):
    extension_exists =  '.' in filename
    extension_valid = filename.rsplit(".")[-1].lower() in ALLOWED_EXTENSIONS

    return extension_exists and extension_valid

def extract_text_from_pdf(filename):
    text = ""
    reader = PdfReader(filename)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(filename):
    doc = docx.Document(filename)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return "\n".join(text)
