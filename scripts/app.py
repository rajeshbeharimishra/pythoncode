import json
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError

app = Flask(__name__)
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt35turbo', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [{"role": "user", "content": user_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response.choices[0].message["content"]
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)
