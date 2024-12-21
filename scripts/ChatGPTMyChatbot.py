import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "I am a financial expert who specializes in real estate investment advice and negotiations"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)
