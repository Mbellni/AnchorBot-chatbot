from .text_utils import TextPauses
from .constants import *
import time
from colorama import Fore, Style
from .grounding import ask_grounding

class BreathingExercise:
    def __init__(self, breath_count=4, repeat_count=3, delay=1):
        self.breath_count = breath_count
        self.repeat_count = repeat_count
        self.delay = delay

    def count_down(self, phase):
        displayer = TextPauses(f"{Fore.GREEN}{phase}{Style.RESET_ALL}")
        displayer.display()
        for i in range(self.breath_count, 0, -1):
            displayer = TextPauses(f"{Fore.GREEN}{i}{Style.RESET_ALL}")
            displayer.display()
            time.sleep(self.delay)

    def perform(self):
        for cycle in range(1, self.repeat_count + 1):
            displayer = TextPauses(f"\n{Fore.GREEN}Cycle {cycle} of {self.repeat_count}{Style.RESET_ALL}")
            displayer.display()
            self.count_down("Breathing in...")
            self.count_down("Holding...")
            self.count_down("Breathing out...")
            time.sleep(1)

def ask_breathing_1(classifier):
    displayer = TextPauses(QUESTION_BREATHING_1)
    displayer.display()
    answer = input("").strip().lower()
    if answer == "yes":
        displayer = TextPauses(BREATHING_DETAILS)
        displayer.display()
        ask_breathing2(classifier)
    elif answer == "skip":
        ask_grounding(classifier)
    else:
        displayer = TextPauses(RETRY_YES_SKIP)
        displayer.display()
        time.sleep(2)
        ask_breathing_1(classifier)

def ask_breathing2(classifier):
    displayer = TextPauses(QUESTION_BREATHING_START)
    displayer.display()
    answer = input("").strip().lower()
    if answer == "start":
        BreathingExercise().perform()
        displayer = TextPauses(AFTER_BREATHING_MSG)
        displayer.display()
        time.sleep(2)

        displayer = TextPauses(QUESTION_FEELING_AFTER_BREATHING)
        displayer.display()
        feeling_input = input("").strip()

        sentiment = classifier.classify(feeling_input)
        displayer = TextPauses(RESPONSES_SENTIMENT.get(sentiment, RESPONSES_SENTIMENT["default"]))
        displayer.display()
        time.sleep(3)
        ask_breathing_repeat(classifier)
    else:
        displayer = TextPauses(RETRY_START)
        displayer.display()
        time.sleep(2)
        ask_breathing2(classifier)

def ask_breathing_repeat(classifier):
    displayer = TextPauses(REPEAT_BREATHING_PROMPT)
    displayer.display()
    displayer = TextPauses(REPEAT_BREATHING_Q)
    displayer.display()
    answer = input("").strip().lower()
    if answer == "yes":
        ask_breathing2(classifier)
    elif answer == "no":
        displayer = TextPauses(ACK_NO_REPEAT)
        displayer.display()
        time.sleep(1)
        ask_grounding(classifier)
    else:
        displayer = TextPauses(RETRY_YES_NO)
        displayer.display()
        time.sleep(2)
        ask_breathing_repeat(classifier)

