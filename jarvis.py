import pyttsx3
import random

class Jarvis():

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english')
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)

    def run(self, word):
        hello_collection = [
            'Hello',
            'Hi',
            'Hello Jarvis',
            'Hi Jarvis',
        ]
        if word in hello_collection:
            self.engine.say("Hello! I am Jarvis. How can I help you?")
            self.engine.runAndWait()

jarvis = Jarvis()
hello_collection = [
    'Hello',
    'Hi',
    'Hello Jarvis',
    'Hi Jarvis',
]
for i in range(5):
    word = random.choice(hello_collection)
    print(word)
    jarvis.run(word)
