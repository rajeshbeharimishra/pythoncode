import openai

openai.api_key = ""

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Explain Newton's laws of motion"}])
print(completion.choices[0].message.content)
