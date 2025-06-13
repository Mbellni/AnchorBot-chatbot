import time
from .text_utils import TextPauses
from .constants import *
from .cafes import CafeLogic

def ask_grounding():
    displayer = TextPauses(GROUNDING_INTRO)
    displayer.display()

    question = input(GROUNDING_PROMPT).strip().lower()
    if question == "start":
        displayer = TextPauses(GROUNDING_EXERCISE)
        displayer.display()
        ask_continue()
    elif question == "skip":
        ask_positive_affirmations()
    else:
        print(RETRY_START_SKIP)
        time.sleep(2)
        ask_grounding()

def ask_continue():
    question_continue = input(CONTINUE_PROMPT).strip().lower()
    if question_continue == "continue":
        print(CONTINUE_ACK)
        time.sleep(3)
        ask_positive_affirmations()
    else:
        print(RETRY_CONTINUE)
        time.sleep(2)
        ask_continue()

def ask_positive_affirmations():
    print(POSITIVE_INTRO)
    time.sleep(4)
    choice = input(AFFIRMATIONS_START_PROMPT).strip().lower()
    if choice == "start":
        displayer = TextPauses(AFFIRMATIONS_LIST)
        displayer.display()
        ask_feeling_affirmations()
    elif choice == "skip":
        ask_cafe()
    else:
        print(RETRY_START_SKIP)
        time.sleep(2)
        ask_positive_affirmations()

def ask_feeling_affirmations():
    question = input(AFFIRMATION_CHOICE_PROMPT).strip()
    response = AFFIRMATION_RESPONSES.get(question)
    if response:
        print(response)
        time.sleep(4)
        print(POSITIVE_REINFORCEMENT)
        time.sleep(3)
        print(CAFE_INTRO)
        time.sleep(5)
        print(CAFE_PRIVACY_NOTE)
        time.sleep(10)
        ask_cafe()
    else:
        print(RETRY_AFFIRMATION_CHOICE)
        time.sleep(3)
        ask_feeling_affirmations()

def ask_cafe():
    question = input(CAFE_PROMPT).strip().lower()
    if question == "yes":
        chatbot = CafeLogic()
        results_found = chatbot.run()
        time.sleep(3)
        if results_found:
            print(CAFE_FOUND)
        else:
            print(CAFE_NOT_FOUND)
        time.sleep(3)
        ask_conclusion(chatbot.classifier)
    elif question == "conclude":
        displayer = TextPauses(CAFE_CONCLUDE_TEXT)
        displayer.display()
        ask_conclusion(None)
    else:
        print(RETRY_CAFE_PROMPT)
        time.sleep(2)
        ask_cafe()

def ask_conclusion(classifier):
    question_conclusion_feel = input(CONCLUSION_PROMPT).strip()
    if classifier:
        sentiment = classifier.classify(question_conclusion_feel)
        print(RESPONSES_SENTIMENT.get(sentiment, RESPONSES_SENTIMENT["default"]))
    else:
        print(CONCLUSION_GENERIC_RESPONSE)
    time.sleep(3)
    displayer = TextPauses(CLOSING_RECOMMENDATIONS)
    displayer.display()
    print(FINAL_GOODBYE)
    time.sleep(2)
    exit()