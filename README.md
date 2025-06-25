# Anemia Predictor Web Application
This is a Flask-based web application that predicts whether a person is anemic based on input features like hemoglobin, MCH, MCHC, MCV and gender. This model is trained using machine learning and integrated into the UI to make live prediction.
File structure:
Flask/
│
├── app.py # Main Flask app script
├── model.pkl # Trained machine learning model
│
├── forms/
│ └── anemia_form.py # WTForms for collecting input data
│
├── static/
│ ├── style.css # CSS styles
│ ├── favicon.ico # Browser tab icon
│ └── images/
│ ├── background.jpg # Background image for index.html
│ └── result.jpg # Background for result page
│
├── templates/
│ ├── index.html # Home page with input form
│ └── predict.html # Result display page

Here is the list of technologies used in this project:

*Python
*Flask
*Scikit-learn
*Pandas / NumPy / matplotlib / seaborn
*HTML + CSS + Jinja2
*Flask-WTF
