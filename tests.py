# question_conclusion_feel = input("""
# Before we wrap up, I’d love to hear—
# how are you feeling after our session?
# \n""")
# print("""response I hear you, and thank you for sharing
# that with me. It’s all part of the
# journey.""")





# from colorama import Fore, Style

# message = f"""
# {Fore.GREEN}Welcome to the chatbot!{Style.RESET_ALL}
# Here are your options:
# {Fore.YELLOW}1. Start a new conversation{Style.RESET_ALL}
# {Fore.CYAN}2. Learn about mindfulness{Style.RESET_ALL}
# {Fore.GREEN}3. Exit the chatbot

# Please choose an option.
# """
# print(message)


# import re
# import time
# from colorama import Fore, Style


# #test of pauses logic with classes
# class TextPauses:
#     def __init__(self, text, pause=3):

#         self.text = text
#         self.pause = pause
        
    
#     def display(self):

#         sections = re.split(r'(\n\s*\n)', self.text) 

#         for section in sections:

#             if section.strip():  
#                 print(section.strip())
               
#                 time.sleep(self.pause)

#             else:
#                 print("") 



# def start_convo():

#     intro_text = f"""{Fore.GREEN}
# Hello, I’m TRAC, your Tranquility, Reflection and 
# Awareness Chatbot.

# I’m here to help you find moments of calm and clarity.

# Whether you’re feeling overwhelmed or just need to 
# unwind a bit, these strategies can be a great way to 
# restore balance.
# {Style.RESET_ALL}"""
    
#     # Instantiate the TextDisplayer class
#     displayer = TextPauses(intro_text)
    
#     # Display the text with pauses
#     displayer.display()

#     # Continue with the rest of the program
#     print(f"{Fore.CYAN}Let’s begin the relaxation exercises now.{Style.RESET_ALL}")



# start_convo()




# import time

# class BreathingExercise:
#     def __init__(self, breath_count=5, repeat_count=3, delay=1):

#         self.breath_count = breath_count
#         self.repeat_count = repeat_count
#         self.delay = delay

#     def count_down(self, phase):

#         print(f"{phase}...")
#         for i in range(self.breath_count, 0, -1):
#             print(i)
#             time.sleep(self.delay)

#     def perform(self):

#         for cycle in range(1, self.repeat_count + 1):
#             print(f"\nCycle {cycle} of {self.repeat_count}")
#             self.count_down("Breathing in")
#             self.count_down("Holding")
#             self.count_down("Breathing out")
#         print("\nBreathing exercise complete! Well done.")


# def breathing_1():
#     print("Welcome to your guided breathing session!")
#     # Create an refrence of BreathingExercise
#     breathing = BreathingExercise(breath_count=5, repeat_count=3, delay=1)
#     # Do breathing exercise
#     breathing.perform()

# breathing_1()


from chatbot_base import ChatbotBase
import time
from colorama import Fore, Style
import re
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


#start of classes
class TextPauses:
    def __init__(self, text, pause=3):

        self.text = text
        self.pause = pause
        
    
    def display(self):

        sections = re.split(r'(\n\s*\n)', self.text) 

        for section in sections:

            if section.strip():  
                print(section.strip())
               
                time.sleep(self.pause)

            else:
                print("") 






def ask_grounding():
    #ask user to start or skip grounding exercise
    intro_grounding = """Let’s try something a bit different instead. 

We’ll move on to a grounding exercise that can 
help bring you into the present moment and find 
a sense of calm. 
"""
    displayer = TextPauses(intro_grounding) #adds pauses between paragraphs
    displayer.display()


    question_grounding_start = input(f"""{Fore.GREEN}
Please type “start” or “skip”.\n
{Style.RESET_ALL}""")
    
    

#if start, show grounding exercise
    if question_grounding_start == ("start"):
        grounding_ex = (f"""{Fore.GREEN}
Let’s try a grounding exercise called “5-4-3-2-1.” 
This helps bring you to the present moment.
              
- Name **5 things** you can see around you.
- Name **4 things** you can touch.
- Name **3 things** you can hear.
- Name **2 things** you can smell.
- And finally, name **1 thing** you can taste.
{Style.RESET_ALL}""")
        
        displayer = TextPauses(grounding_ex) #adds pauses between paragraphs
        displayer.display()

        #time.sleep(2)#pause continue option shows up
        #ask_continue()



ask_grounding()