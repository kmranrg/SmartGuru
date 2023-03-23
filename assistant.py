import openai

openai.api_key = str(open("token.txt").read())

class SmartGurucool():

    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def SmartGuruResponse(self, user_text):
        self.user_text = user_text

        while True:

            # if user says stop, then breaking the loop
            if self.user_text == "stop":
                break
            
            # storing the user question in the messages list
            self.messages.append({"role": "user", "content": self.user_text})

            # getting the response from OpenAI API
            response= openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages
            )

            # appending the generated response so that AI remebers past responses
            self.messages.append({"role":"assistant", "content":str(response['choices'][0]['message']['content'])})
            
            # returning the response
            print(response['choices'][0]['message']['content'])
            return response['choices'][0]['message']['content']