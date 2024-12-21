from flask import Flask, render_template, request, jsonify, session
from flask_session import Session  # Import Flask-Session
import openai
import os
import random
import string

app = Flask(__name__)

def generate_random_string(length):
    # Define the characters that can be used in the random string
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices() to generate a random string of the specified length
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

# Configure your OpenAI API key
api_key = "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"
app.config['SESSION_TYPE'] = 'filesystem'
secretkey = generate_random_string(20)
app.secret_key = secretkey
Session(app)

# Initialize OpenAI API client
openai.api_key = api_key

@app.route('/')
def index():
    # Initialize the chat log in the session if it doesn't exist
    if 'chat_log' not in session:
        session['chat_log'] = ''
    return render_template('myapp.html')

@app.route('/chat', methods=['POST'])

def chat():
    user_message = request.form['user_message']
    chat_log = session['chat_log'] + f'User: {user_message}\n'
    
    # Generate a response from OpenAI's GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=chat_log,
        max_tokens=50  # Adjust as needed
    )

    chat_log += f'{response.choices[0].text}\n'
    session['chat_log'] = chat_log

    return jsonify({'response': response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True)
