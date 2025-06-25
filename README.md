# Project: ASKIFY a Chatbot 

## Description

This project is a Flask-based chatbot integrated with fuzzy matching using the `fuzzywuzzy` library. The chatbot responds to user queries with a focus on providing instant assistance. The `fuzzywuzzy` library helps match user inputs with predefined answers for flexible query handling.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- fuzzywuzzy

## Setup Instructions

### 1. Install Visual Studio Code (VSCode)
If you haven’t already, [download and install Visual Studio Code](https://code.visualstudio.com/).

### 2. Install Python
Ensure that Python 3.x is installed on your system. If not, download and install it from [here](https://www.python.org/downloads/).

### 3. Clone the Project
Clone the repository or download the project files to your local system.

### 4. Install Dependencies
Install all the required packages using `pip`:
  you can manually install the required packages:
```bash
pip install Flask flask_cors fuzzywuzzy
```

### 5. Running the Application
Run the Flask app by executing:
```bash
python app.py
```

This will start the server, and you can access the chatbot by opening `http://127.0.0.1:5000` in your browser.

### 6. Testing the Chatbot
Once the server is running, you can interact with the chatbot through the HTML page that is served by Flask. The page allows you to input a query and receive a response.

- Open your browser and go to http://127.0.0.1:5000. The HTML page for the chatbot will be displayed.
- On the page, you can input a query like "Admission details" in the text input box.
- Once you submit the query, the chatbot will respond based on the predefined answers.

## Project Structure

```
/project-root
│
├── app.py                # Main Flask application file
├── requirements.txt      # List of required dependencies
├── index.html            # HTML file for the chatbot interface
├── script.js             # JavaScript file to handle interactions and AJAX requests
└── styles.css            # CSS file for styling the chatbot page

```

Video Demo Link: https://www.linkedin.com/posts/telidevara_miniproject-askify-chatbot-activity-7343517792345694209-5SE6?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD6GP6UB7FIFXQO9jnEYv7sYnYPoLDj2vQI
