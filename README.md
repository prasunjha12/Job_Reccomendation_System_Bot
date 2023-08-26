# Job_Reccomendation_System_Bot

Welcome to the Job Recommendation System Bot repository! This project is a Flask-based web application that uses Natural Language Processing (NLP) to match users with suitable job openings based on their skills and experience.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Job_Reccomendation_System_Bot.git
   cd Job_Reccomendation_System_Bot
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Flask server:

bash
Copy code
python chatbot.py
Open your web browser and navigate to http://127.0.0.1:5000/.

Enter your skills separated by commas, followed by your experience level (e.g., Python, Data Analysis, 3).

Click the "Find Jobs" button.

The bot will display a list of suitable job openings based on your input.

Repository Contents
chatbot.py: The Flask application that handles user input and provides job suggestions.
index.html: The HTML file containing the web interface for user input.
style.css: The CSS file containing styling for the web interface.
script.js: The JavaScript file responsible for making requests to the Flask server.
job_descriptions.json: JSON file containing sample job descriptions for matching.

Dependencies
Flask: Web framework for building the user interface.
spaCy: Natural Language Processing library for skill extraction.
openai: OpenAI API library for job matching.
Contributing
Contributions are welcome! Feel free to fork the repository, make enhancements, and submit pull requests.

License
This project is licensed under the MIT License.
