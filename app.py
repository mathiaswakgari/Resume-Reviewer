import os
from flask import Flask, request, jsonify, render_template
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
nlp = spacy.load("en_core_web_sm_extended")

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

def analyse_text(text):
    doc  = nlp(text)
    prog_languages = [ent.text for ent in doc.ents if ent.label_ == "PROGRAMMING_LANGUAGE"]
    tools = [ent.text for ent in doc.ents if ent.label_ == "TOOL"]
    spoken_languages = [ent.text for ent in doc.ents if ent.label_ == "LANGUAGE"]
    technologies_used = [ent.text for ent in doc.ents if ent.label_ == "TECHNOLOGY"]
    return {
        "word_count": len(text.split()),
        "entities": [(ent.text, ent.label_) for ent in doc.ents],
        "programming_languages": prog_languages,
        "tools_used": tools,
        "spoken_languages": spoken_languages,
        "technologies_used": technologies_used
    }

@app.route('/upload')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        
        if filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.lower().endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            return jsonify({"error": "Unsupported file type"}), 400
        
        
        skills = analyse_text(text)
        return jsonify(skills)
    else:
        return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)