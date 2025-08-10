# QR Code Generator from Text/Links
A simple Flask web service that generates QR codes from text or URLs. The interface is built with Bootstrap 5.

## Features
* Input text or URL via a form
* Server-side QR code generation
* Display QR code directly on the page
* Responsive and clean Bootstrap 5 interface
* Easy to deploy on Render.com or any Python hosting platform

## Technologies
* Python 3
* Flask
* qrcode (for QR code generation)
* Bootstrap 5 (via CDN)

## Installation and Local Run
Clone the repository or download the project files.
* (Recommended) Create and activate a virtual environment:
```commandline
    python -m venv venv
    source venv/bin/activate    # Linux/Mac
    venv\Scripts\activate       # Windows

```

## Install dependencies:
```commandline
   pip install -r requirements.txt
```

## Run the application:
```commandline
   python app.py

```
# Deploying on Render.com
- Push your code to a GitHub/GitLab repository.
- Create a new Web Service on Render.com.
- Select a Python Flask project.
- Link your repository and branch.
- In Build Command enter:
```commandline
   pip install -r requirements.txt
   
   In Start Command enter:
   gunicorn app:app
```
Deploy and your app will be live at the Render URL.

## Project Structure
```commandline
/
├── app.py              # Main Flask application file
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # HTML template with Bootstrap

```