import time
import sys
from .text_utils import TextPauses
from .constants import *
from .breathing import ask_breathing_1
from .sentiment import Feelings


def start_conversation(classifier):
    displayer = TextPauses(INTRO_TEXT)
    displayer.display()
    time.sleep(1)  # Optional: short pause after the intro finishes

    answer = input(QUESTION_START).strip().lower()
    if answer == "yes":
        displayer = TextPauses(BREATHING_INTRO)
        displayer.display()
        ask_breathing_1(classifier)
    elif answer == "no":
        displayer = TextPauses(EXIT_MESSAGE)
        displayer.display()
        sys.exit()
    else:
        displayer = TextPauses(RETRY_YES_NO)
        displayer.display()
        time.sleep(2)
        start_conversation(classifier)



# Initialize the classifier
classifier = Feelings()

# Entry point for running the chatbot
def run():
    print("Chatbot is running...\n")
    start_conversation(classifier)


    
