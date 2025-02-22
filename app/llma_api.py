# This example is the new way to use the OpenAI lib for python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("LLAMA_API_TOKEN"),
    base_url="https://api.llama-api.com"
)

response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ],
)

#print(response)
# print(response.model_dump_json(indent=2))
# print(response.choices[0].message.content)

# from openai import OpenAI



response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "I love you."}
    ],
    tools = [
      {
        'type': 'function',
        'function':
            {'name': 'information_extraction',
            'description': 'Extracts the relevant information from the user message.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'sentiment': {'title': 'sentiment', 'type': 'string', 'description': 'the sentiment encountered in the passage'},
                    'aggressiveness': {'title': 'aggressiveness', 'type': 'integer', 'description': 'a 0-10 score of how aggressive the passage is'},
                    'language': {'title': 'language', 'type': 'string', 'description': 'the language of the passage'},
                }, 'required': []
            }
          }
      }
    ]
)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.function_call)