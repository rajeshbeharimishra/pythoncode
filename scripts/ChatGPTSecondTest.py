import openai

openai.api_key = "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"

completion=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant who is trying to find a user's favorite color."},
        {"role": "system", "content": "Until the user tell's their favorite color, keep asking them for it."},
        {"role": "user", "content": "How are you doung today?"}
    ]
)
print(completion.choices[0].message.content)
