import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines as well
        prompt=prompt,
        max_tokens=50,  # Adjust as needed
        temperature=0.7,  # Adjust to control the randomness of responses
    )
    
    return response.choices[0].text

# Start a conversation with the chatbot
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    conversation = f'You: {user_input}\nChatbot:'
    response = chat_with_bot(conversation)
    print(response)
