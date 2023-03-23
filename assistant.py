import openai

openai.api_key = str(open("token.txt").read())

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

status = True

while status != False:
  user_question = input("What do you wanna ask?")

  # if user says stop, then breaking the loop
  if user_question == "stop":
    break
  
  # storing the user question in the messages list
  messages.append({"role": "user", "content": user_question})

  # getting the response from OpenAI API
  response= openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  # appending the generated response so that AI remebers past responses
  messages.append({"role":"assistant", "content":str(response['choices'][0]['message']['content'])})
  print(response['choices'][0]['message']['content'])

for i in messages:
  print(i)