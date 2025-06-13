from chatbot.text_utils import TextPauses
from chatbot.constants import *
import time
from colorama import Fore, Style
from chatbot.grounding import ask_grounding

class BreathingExercise:
    def __init__(self, breath_count=4, repeat_count=3, delay=1):
        self.breath_count = breath_count
        self.repeat_count = repeat_count
        self.delay = delay

    def count_down(self, phase):
        print(f"{Fore.GREEN}{phase}{Style.RESET_ALL}")
        for i in range(self.breath_count, 0, -1):
            print(f"{Fore.GREEN}{i}{Style.RESET_ALL}")
            time.sleep(self.delay)

    def perform(self):
        for cycle in range(1, self.repeat_count + 1):
            print(f"\n{Fore.GREEN}Cycle {cycle} of {self.repeat_count}{Style.RESET_ALL}")
            self.count_down("Breathing in...")
            self.count_down("Holding...")
            self.count_down("Breathing out...")
            time.sleep(1)

def ask_breathing_1(classifier):
    answer = input(QUESTION_BREATHING_1).strip().lower()
    if answer == "yes":
        displayer = TextPauses(BREATHING_DETAILS)
        displayer.display()
        ask_breathing2(classifier)
    elif answer == "skip":
        ask_grounding()
    else:
        print(RETRY_YES_SKIP)
        time.sleep(2)
        ask_breathing_1(classifier)

def ask_breathing2(classifier):
    answer = input(QUESTION_BREATHING_START).strip().lower()
    if answer == "start":
        BreathingExercise().perform()
        print(AFTER_BREATHING_MSG)
        time.sleep(2)

        feeling_input = input(QUESTION_FEELING_AFTER_BREATHING)
        sentiment = classifier.classify(feeling_input)

        print(RESPONSES_SENTIMENT.get(sentiment, RESPONSES_SENTIMENT["default"]))
        time.sleep(3)
        ask_breathing_repeat(classifier)
    else:
        print(RETRY_START)
        time.sleep(2)
        ask_breathing2(classifier)

def ask_breathing_repeat(classifier):
    print(REPEAT_BREATHING_PROMPT)
    answer = input(REPEAT_BREATHING_Q).strip().lower()
    if answer == "yes":
        ask_breathing2(classifier)
    elif answer == "no":
        print(ACK_NO_REPEAT)
        time.sleep(1)
        ask_grounding()
    else:
        print(RETRY_YES_NO)
        time.sleep(2)
        ask_breathing_repeat(classifier)