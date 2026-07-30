"""
CodeAlpha Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to a set of predefined
user inputs using if-elif logic and keyword matching.
"""

import random

GREETINGS = ["hello", "hi", "hey", "hola"]
FAREWELLS = ["bye", "goodbye", "see you", "exit", "quit"]

RESPONSES = {
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "your name": ["I'm CodeAlpha Bot, your friendly assistant!", "You can call me CodeAlpha Bot."],
    "what can you do": [
        "I can chat with you about simple things like greetings, how you're doing, and more!"
    ],
    "thank": ["You're welcome!", "No problem at all!"],
    "help": ["Try saying hello, asking how I am, or asking my name!"],
}


def get_response(user_input):
    text = user_input.lower().strip()

    if not text:
        return "Please say something!"

    if any(word in text for word in FAREWELLS):
        return "Goodbye! Have a great day!"

    if any(word in text for word in GREETINGS):
        return random.choice(["Hi!", "Hello there!", "Hey! How can I help you today?"])

    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies)

    return "Sorry, I don't understand that. Try saying 'hello' or ask 'how are you'."


def chat():
    print("CodeAlpha Chatbot")
    print("Type 'bye' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if any(word in user_input.lower() for word in FAREWELLS):
            break


if __name__ == "__main__":
    chat()
