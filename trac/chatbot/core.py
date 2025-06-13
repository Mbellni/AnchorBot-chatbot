import time
import sys
from .text_utils import TextPauses
from .constants import *
from .breathing import ask_breathing_1
from .sentiment import Feelings


def start_conversation(classifier):
    print(INTRO_TEXT)
    time.sleep(3)
    answer = input(QUESTION_START).strip().lower()
    if answer == "yes":
        displayer = TextPauses(BREATHING_INTRO)
        displayer.display()
        ask_breathing_1(classifier)
    elif answer == "no":
        print(EXIT_MESSAGE)
        sys.exit()
    else:
        print(RETRY_YES_NO)
        time.sleep(2)
        start_conversation(classifier)


# Initialize the classifier
classifier = Feelings()

# Entry point for running the chatbot
def run():
    print("Chatbot is running...\n")
    start_conversation(classifier)


    
