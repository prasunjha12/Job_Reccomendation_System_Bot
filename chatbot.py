import os
import openai
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

openai.api_key = "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"

def match_jobs(user_skills, user_experience, job_descriptions):
    suitable_jobs = []

    for job in job_descriptions:
        required_skills = job.get("Skills Required", [])
        required_experience = job.get("Experience Required", "")

        matching_skills = [skill for skill in user_skills if skill in required_skills]
        if required_experience.isdigit() and int(required_experience) <= user_experience:
            matching_experience = True
        else:
            matching_experience = False

        if matching_skills and matching_experience:
            suitable_jobs.append(job)

    return suitable_jobs

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['POST'])
def chatbot():
    user_input = request.form['user_skills']
    user_skills = user_input.split(',')
    
    if len(user_skills) < 2 or not user_skills[-1].isdigit():
        response = "Please provide a comma-separated list of your skills followed by your experience level (e.g. Python,Data Analysis,3)."
        return jsonify({'response': response})

    user_experience = int(user_skills.pop())

    with open("job_descriptions.json", "r") as f:
        job_descriptions = json.load(f)

    suitable_jobs = match_jobs(user_skills, user_experience, job_descriptions)

    if suitable_jobs:
        response = "Based on your skills and experience, here are the most suitable jobs:\n\n"
        for job in suitable_jobs:
            response += f"**Role:** {job['Role']}\n"
            response += f"**Company:** {job['Company Name']}\n"
            response += f"**Location:** {job['Location']}\n\n"
    else:
        response = "I'm sorry, but there are currently no job openings that match your skills and experience."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)