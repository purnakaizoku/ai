# utils.py
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
