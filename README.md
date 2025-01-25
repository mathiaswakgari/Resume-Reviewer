# Resume Analyzer

**Resume Analyzer** is a Flask-based application that processes resumes in PDF and DOCX formats, extracts relevant information using NLP, and categorizes the resumes based on experience level, skills, and other details. The project also includes a Vite-based React frontend for an enhanced user experience.

## Features

- **Upload Resumes**: Supports PDF and DOCX formats.
- **Text Extraction**: Extracts text from uploaded files.
- **NLP Analysis**: Utilizes spaCy for Named Entity Recognition (NER).
- **Resume Categorization**: Categorizes resumes based on:
  - Experience level (Junior, Mid-level, Senior)
  - Skill type (e.g., Software Developer, Data Scientist, Project Manager)
  - Scoring system to rank resumes.
- **Frontend**: React application for uploading resumes and displaying results.
- **REST API**: Provides an endpoint for file uploads and analysis.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Frontend](#frontend)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [License](#license)

---

## Installation

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the required spaCy model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Create the upload folder:

   ```bash
   mkdir uploads
   ```

6. Run the backend application:

   ```bash
   python app.py
   ```

The backend will be available at `http://127.0.0.1:5000/`.

### Frontend Setup

1. Navigate to the `frontend` folder:

   ```bash
   cd frontend
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

The frontend will be available at `http://127.0.0.1:5173/`.

---

## Usage

### Web Interface

1. Start both the backend and frontend servers.
2. Open the frontend application in your browser at `http://127.0.0.1:5173/upload`.
3. Upload a PDF or DOCX file containing a resume.
4. View the analysis results on the page.

### API Endpoint

**Endpoint**: `/upload`

**Method**: `POST`

**Request**:

- `file`: Multipart file upload (PDF or DOCX).

**Response**:

```json
{
  "experience_level": "Senior",
  "skill_level": "Software Developer",
  "score": 95,
  "details": {
    "full_name": ["John Doe"],
    "tech_stacks": ["Python", "JavaScript"],
    "experience": ["5 years"],
    "institute": ["MIT"],
    "languages_spoken": ["English", "French"],
    "email": ["johndoe@example.com"],
    "phone_number": ["123-456-7890"]
  }
}
```

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: React (Vite)
- **NLP**: spaCy
- **PDF Parsing**: PyPDF2
- **DOCX Parsing**: python-docx
- **Other Libraries**:
  - Flask-CORS
  - Werkzeug (for file handling)

---

## Folder Structure

```
resume-analyzer/
|├── app.py              # Main application file
|├── frontend/          # React frontend folder
|├── templates/         # HTML templates for Flask
|├── uploads/           # Uploaded files folder
|├── requirements.txt   # Python dependencies
|└── README.md          # Project documentation
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## Author

Created by Mathias Wakgari(https://github.com/mathiaswakgari).
