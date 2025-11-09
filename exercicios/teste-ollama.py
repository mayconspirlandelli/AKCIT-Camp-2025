from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1:8b', messages=[
  {
    'role': 'user',
    'content': 'Qual a capital do Brasil?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)


# from ollama import chat

# response = chat(
#   model='qwen3',
#   messages=[{'role': 'user', 'content': 'How many letter r are in strawberry?'}],
#   think=True,
#   stream=False,
# )

# print('Thinking:\n', response.message.thinking)
# print('Answer:\n', response.message.content)