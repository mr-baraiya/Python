
from openai import OpenAI 

client = OpenAI(
    api_key= "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"
)

response = client.chat.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant name Jarvis skilled in general task lik Alexa and Google Cloud."},
        {"role": "user", "content": "what is codeing?"},
    ]
)

print(response["choices"][0]["message"]["content"])