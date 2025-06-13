import time
from .text_utils import TextPauses
from .constants import *
from .cafes import CafeLogic

def ask_grounding(classifier):
    displayer = TextPauses(GROUNDING_INTRO)
    displayer.display()

    displayer = TextPauses(GROUNDING_PROMPT)
    displayer.display()
    question = input("> ").strip().lower()

    if question == "start":
        displayer = TextPauses(GROUNDING_EXERCISE)
        displayer.display()
        ask_continue(classifier)
    elif question == "skip":
        ask_positive_affirmations(classifier)
    else:
        displayer = TextPauses(RETRY_START_SKIP)
        displayer.display()
        time.sleep(2)
        ask_grounding(classifier)

def ask_continue(classifier):
    displayer = TextPauses(CONTINUE_PROMPT)
    displayer.display()
    question_continue = input("> ").strip().lower()

    if question_continue == "continue":
        displayer = TextPauses(CONTINUE_ACK)
        displayer.display()
        time.sleep(1)
        ask_positive_affirmations(classifier)
    else:
        displayer = TextPauses(RETRY_CONTINUE)
        displayer.display()
        time.sleep(2)
        ask_continue(classifier)

def ask_positive_affirmations(classifier):
    displayer = TextPauses(POSITIVE_INTRO)
    displayer.display()
    time.sleep(1)

    displayer = TextPauses(AFFIRMATIONS_START_PROMPT)
    displayer.display()
    choice = input("> ").strip().lower()

    if choice == "start":
        displayer = TextPauses(AFFIRMATIONS_LIST)
        displayer.display()
        time.sleep(1)
        ask_feeling_affirmations(classifier)
    elif choice == "skip":
        ask_cafe(classifier)
    else:
        displayer = TextPauses(RETRY_START_SKIP)
        displayer.display()
        time.sleep(2)
        ask_positive_affirmations(classifier)

def ask_feeling_affirmations(classifier):
    displayer = TextPauses(AFFIRMATION_CHOICE_PROMPT)
    displayer.display()
    question = input("> ").strip()
    response = AFFIRMATION_RESPONSES.get(question)

    if response:
        displayer = TextPauses(response)
        displayer.display()
        time.sleep(1)

        displayer = TextPauses(POSITIVE_REINFORCEMENT)
        displayer.display()
        time.sleep(1)

        displayer = TextPauses(CAFE_INTRO)
        displayer.display()

        displayer = TextPauses(CAFE_PRIVACY_NOTE)
        displayer.display()

        ask_cafe(classifier)
    else:
        displayer = TextPauses(RETRY_AFFIRMATION_CHOICE)
        displayer.display()
        time.sleep(3)
        ask_feeling_affirmations(classifier)

def ask_cafe(classifier):
    displayer = TextPauses(CAFE_PROMPT)
    displayer.display()
    question = input("> ").strip().lower()

    if question == "yes":
        chatbot = CafeLogic()
        results_found = chatbot.run()
        time.sleep(2)

        displayer = TextPauses(CAFE_FOUND if results_found else CAFE_NOT_FOUND)
        displayer.display()
        time.sleep(1)

        ask_conclusion(classifier)

    elif question == "conclude":
        displayer = TextPauses(CAFE_CONCLUDE_TEXT)
        displayer.display()
        ask_conclusion(None)
    else:
        displayer = TextPauses(RETRY_CAFE_PROMPT)
        displayer.display()
        time.sleep(2)
        ask_cafe(classifier)

def ask_conclusion(classifier):
    displayer = TextPauses(CONCLUSION_PROMPT)
    displayer.display()
    question_conclusion_feel = input("> ").strip()

    if classifier:
        sentiment = classifier.classify(question_conclusion_feel)
        displayer = TextPauses(RESPONSES_SENTIMENT.get(sentiment, RESPONSES_SENTIMENT["default"]))
        displayer.display()
    else:
        displayer = TextPauses(CONCLUSION_GENERIC_RESPONSE)
        displayer.display()

    time.sleep(1)

    displayer = TextPauses(CLOSING_RECOMMENDATIONS)
    displayer.display()

    displayer = TextPauses(FINAL_GOODBYE)
    displayer.display()

    time.sleep(2)
    exit()

