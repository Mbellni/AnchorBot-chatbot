from chatbot.text_utils import TextPauses
from chatbot.constants import *
from chatbot.breathing import ask_breathing_1
import time
import sys

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





    
