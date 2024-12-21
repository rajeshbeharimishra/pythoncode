import json
from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "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"
gptchatbot = Flask(__name__)

messages = [{"role": "assistant", "content": "I am OpenAI based Assistant to answer real estate questions"}]
messages.append({"role": "system", "content": "Produce the output in a numbered list separated by a line"})

@gptchatbot.route('/')
def index():
    return render_template('gptchatbot.html')

@gptchatbot.route('/gpt35turbo', methods=['GET', 'POST'])

def CustomChatGPT():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "system", "content": "If the question does not relate to real estate say 'I am an assistant to provide answers related to real estate questions only. Sorry !, I do not know the answer to your question'"})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return jsonify(content=ChatGPT_reply)

if __name__ == '__main__':
    gptchatbot.run(debug=True)
