from chatbot_base import ChatbotBase
import time
from colorama import Fore, Style
import re
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

"activate this thing if the lexicon hasnt been downloaded yet"
nltk.downloader.download('vader_lexicon') 

class MyChatbot(ChatbotBase):
    def __init__(self, name="Chatbot"):
        ChatbotBase.__init__(self,name)
        





#Final Iteration
text_explain = """Last few changes after feedback."""






#start of classes
#regex logic that adds pauses between paragraphs with blank spaces
class TextPauses:
    def __init__(self, text, pause=5):

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





#breathing exercise logic. I created with the help of my brother
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
            self.count_down(f"{Fore.GREEN}Breathing in...{Style.RESET_ALL}")
            self.count_down(f"{Fore.GREEN}Holding...{Style.RESET_ALL}")
            self.count_down(f"{Fore.GREEN}Breathing out...{Style.RESET_ALL}")

        
            time.sleep(1)





#Clearly I didn't create this myself... original sript by Arpit Sharma with ChatGPT alterations (https://medium.com/@arpit23sh/discover-nearby-places-with-python-a-geolocation-adventure-770ecc78f13f)
class CafeLogic:
    def __init__(self, max_results=20, user_agent="location_lookup"):
        self.max_results = max_results
        self.geolocator = Nominatim(user_agent=user_agent)

    def get_location_from_postal_code(self, postal_code):
        # Convert postal code to latitude and longitude using geopy Nominatim
        try:
            location = self.geolocator.geocode(postal_code)
            if location:
                return location.latitude, location.longitude
            else:
                print(Fore.GREEN + f"Could not find location for postal code: {postal_code}" + Style.RESET_ALL)
                return None, None
        except Exception as e:
            print(Fore.GREEN + f"Error occurred while fetching location: {e}" + Style.RESET_ALL)
            return None, None

    def find_nearby_cafes(self, lat, lon, radius):
        # Find nearby cafes based on latitude, longitude, and radius
        overpass_url = "http://overpass-api.de/api/interpreter"
        osm_tag = "amenity=cafe"
        
        query = f"""
        [out:json];
        node[{osm_tag}]
          (around:{int(radius * 1000)},{lat},{lon});
        out;
        """

        try:
            response = requests.get(overpass_url, params={'data': query})
            response.raise_for_status()
            data = response.json()

            cafes_found = 0
            if not data['elements']:
                print(Fore.GREEN + "No nearby cafes found within the given radius." + Style.RESET_ALL)
                return False
            else:
                print(Fore.GREEN + f"\nNearby cafes within {radius} mi (maximum {self.max_results} results):" + Style.RESET_ALL)
                for element in data['elements']:
                    if cafes_found >= self.max_results:
                        break
                    
                    place_lat = element['lat']
                    place_lon = element['lon']
                    place_name = element.get('tags', {}).get('name', None)

                    if place_name:
                        place_distance = geodesic((lat, lon), (place_lat, place_lon)).kilometers
                        print(Fore.GREEN + f"{place_name} ({place_distance:.2f} miles)" + Style.RESET_ALL)
                        cafes_found += 1
                if cafes_found == 0:
                    print(Fore.GREEN + "No cafes with a name found in the given radius." + Style.RESET_ALL)
                    return False
            return True
        except requests.RequestException as e:
            print(Fore.GREEN + f"Error: Unable to fetch nearby cafes. Details: {e}" + Style.RESET_ALL)
            return False

    def run(self):
        # Start the chatbot interaction
        while True:
            postal_code = input(f"{Fore.GREEN}Please enter your postal code: {Style.RESET_ALL}")
            lat, lon = self.get_location_from_postal_code(postal_code)
            
            if lat is not None and lon is not None:
                search_radius = float(input(f"{Fore.GREEN}Enter the search radius (type numbers only): {Style.RESET_ALL}"))
                results_found = self.find_nearby_cafes(lat, lon, search_radius)
                return results_found  # Return whether results were found
            else:
                print(Fore.GREEN + "Invalid postal code. Please try again." + Style.RESET_ALL)






class Feelings:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def classify(self, text):
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound < -0.5:
            return 'negative'
        elif compound > 0.5:
            return 'positive'
        else:
            return 'neutral'
    

        

#end of classes





#Introduction         #Found in colorama stuff at https://pypi.org/project/colorama/ and timer at https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
#start of functions and control-flow
text = f"""{Fore.GREEN}
Hello, I’m TRAC, your Tranquility, Reflection and 
Awareness Chatbot.

I’m here to help you find moments of calm and clarity.

Whether you’re feeling overwhelmed or just need to 
unwind a bit, these strategies can be a great way to 
restore balance.
{Style.RESET_ALL}"""

#Use regex to split the text into sections, including the paragraph breaks
sections = re.split(r'(\n\s*\n)', text)


for section in sections:
    #Print only non-empty sections, including blank paragraphs
    if section.strip():
        print(section.strip())
        time.sleep(3)
    else:
        print("")  #Print blank line for whitespace in between prhases

 # another pause before the start of user interaction at the end of the script
time.sleep(1)






def ask_conclusion(classifier):
    #ask user's feeling
    question_conclusion_feel = input(f"""{Fore.GREEN}
Before we wrap up, I’d love to hear—
how are you feeling after our session?
\n{Style.RESET_ALL}""") 
    
    sentiment = classifier.classify(question_conclusion_feel) # classify user's response according to what they're feeling

    if sentiment == 'negative':
        print(f"{Fore.GREEN}It’s okay to not be okay right now.{Style.RESET_ALL}")
    elif sentiment == 'neutral':
        print(f"{Fore.GREEN}I appreciate you telling me that.{Style.RESET_ALL}")
    elif sentiment == 'positive':
        print(f"{Fore.GREEN}That's wonderful to hear!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}It sounds like there’s a lot on your mind.{Style.RESET_ALL}")

    time.sleep(3)#add pause 

    #give user recommendations
    recommendations = (f"""{Fore.GREEN}
Before we part, here are a few small ways to carry calm
with you throughout the day:
          
- Pause for a few deep breaths whenever things feel
overwhelming. Even a moment can help ground you.
          
- Take a brief walk outside or find a quiet corner to
unwind, especially if you’re feeling a bit unsettled.
          
- Practice gratitude by naming one thing you’re thankful
for today. It can bring a surprising amount of peace.
          
Remember, it’s okay to take breaks and prioritize your
well-being. Little moments of care make a big
difference.
{Style.RESET_ALL}""")
    
    displayer = TextPauses(recommendations) #adds pauses between paragraphs
    displayer.display()

    #last line
    print(f"""{Fore.GREEN}
Thank you for being here, and remember, I’m always just a 
message away if you need a moment of calm.
{Style.RESET_ALL}""")
    time.sleep(2)
    exit()
    





def ask_cafe():
    text_conclusion = (f"""{Fore.GREEN}
Thank you for spending this time with me today.

I hope the techniques we explored—whether affirmations, 
breathing exercises, or recommendations—bring you some 
calm and comfort.
{Style.RESET_ALL}""")
    #ask user to find cafe location
    question_start_cafe = input(f"""{Fore.GREEN}
Ready to find a cozy spot? 
Please type “yes” or “conclude”.\n
{Style.RESET_ALL}""")

    #if yes, start cafe logic
    if question_start_cafe == ("yes"):
        
           # Create an instance of CafeFinderChatbot
        chatbot = CafeLogic()

    # Run the chatbot's main interaction
        results_found = chatbot.run()
        time.sleep(3) #pause after the logic runs and before printing question

    # Continue the conversation
        if results_found:
            print(f"{Fore.GREEN}\nI hope you found a cafe that piqued your interest!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}\nI'm sorry I couldn't find any cafes nearby.{Style.RESET_ALL}")

        time.sleep(3)
        ask_conclusion(classifier)

    #if conclude, go to conclusion function
    elif question_start_cafe == ("conclude"):
        displayer = TextPauses(text_conclusion) #adds pauses between paragraphs
        displayer.display()
        ask_conclusion(classifier)
    
    #if other response, give user the options
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “yes” or “conclude.”
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_cafe





#Here it was definitely easier to use the normal time.sleep pauses instead of using regex. It just allowed for more variation
def ask_feeling_affirmations():
    text_positive_reinforcement = f"""{Fore.GREEN}
Great job! Taking a moment to connect with yourself 
like this is a wonderful step.
{Style.RESET_ALL}"""
    text_cafe = f"""{Fore.GREEN}
Now that we’ve set a positive foundation, let’s 
explore some cozy cafes where you can relax, 
reflect, or simply enjoy a peaceful moment.
{Style.RESET_ALL}"""
    text_permission = f"""{Fore.GREEN}
Quick note: our cafe recommendations use a
location-based search to find calming spots
nearby, but rest assured, your location information
is only used temporarily for this purpose and isn’t
stored. Your privacy and confidentiality are always
protected. Also, this task requires wifi connection.
{Style.RESET_ALL}"""
    #ask user to choose favourite phrase
    question_feeling_affirmation = input(f"{Fore.GREEN}Which one speaks to you most? Phrase 1, 2, 3 or 4?\n{Style.RESET_ALL}")

    #if 1, give appropriate answer
    if question_feeling_affirmation == ("1"):
        print(f"""{Fore.GREEN}
Absolutely, you deserve all the peace and calm 
that life has to offer. Embracing that worthiness 
can be so empowering.
{Style.RESET_ALL}""")
        time.sleep(4)
        print(text_positive_reinforcement)
        time.sleep(3)
        print(text_cafe)
        time.sleep(5)
        print(text_permission)
        time.sleep(10)
        ask_cafe()

    #if 2, give appropriate answer
    elif question_feeling_affirmation == ("2"):
        print(f"""{Fore.GREEN}
That’s a beautiful reminder. Your best is more 
than enough, and honoring that can bring such 
a sense of relief.
{Style.RESET_ALL}""")
        time.sleep(4)
        print(text_positive_reinforcement)
        time.sleep(3)
        print(text_cafe)
        time.sleep(5)
        print(text_permission)
        time.sleep(10)
        ask_cafe()

    #if 3, give appropriate answer
    elif question_feeling_affirmation == ("3"):
        print(f"""{Fore.GREEN}
Yes! You have such strength within you. 
Remembering this can help you face any challenge 
that comes your way.
{Style.RESET_ALL}""")
        time.sleep(4)
        print(text_positive_reinforcement)
        time.sleep(3)
        print(text_cafe)
        time.sleep(5)
        print(text_permission)
        time.sleep(10)
        ask_cafe()

    #if 4, give appropriate answer
    elif question_feeling_affirmation == ("4"):
        print(f"""{Fore.GREEN}
Trusting yourself is so powerful. You’re capable and 
resilient, ready to face whatever comes.
{Style.RESET_ALL}""")
        time.sleep(4)
        print(text_positive_reinforcement)
        time.sleep(3)
        print(text_cafe)
        time.sleep(5)
        print(text_permission)
        time.sleep(10)
        ask_cafe()

    #if other response, give user the options 
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type “1”, “2”, “3” or “4”.
{Style.RESET_ALL}""")
        
        time.sleep(3)#pause before asking again
        ask_feeling_affirmations()






def ask_positive_affirmations():
    #ask to start positive affirmations exercise
    print(f"""{Fore.GREEN}
Now, let’s continue with some positive affirmations 
to uplift and encourage you. These can be a wonderful 
way to reinforce a sense of confidence. 
                                        
{Style.RESET_ALL}""")
    
    time.sleep(4)
    
    question_affiramtions_start = input(f"""{Fore.GREEN}
Ready to give it a try?
Please type “start” or “skip”.\n
{Style.RESET_ALL}""")
    
    #if start, show positive affirmations
    if question_affiramtions_start  == ("start"):
        affirmations_list = (f"""{Fore.GREEN}
Here are a few affirmations for today. Repeat each one
slowly to yourself, or let me know which resonates most:
              
1 - “I am worthy of peace and calm.”
                             
2 - “I am doing my best, and that’s enough.”
                             
3 - “I am resilient, strong, and capable.”
                             
4 - “I trust myself to handle what comes my way.”
{Style.RESET_ALL}""")
        
        displayer = TextPauses(affirmations_list) #adds pauses between paragraphs
        displayer.display()
        
        ask_feeling_affirmations()

    #if skip, move on to cafe finding logic
    elif question_affiramtions_start  == ("skip"):
        ask_cafe()  

    #if other response, give user the options 
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “start” or “skip.”
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_positive_affirmations()






def ask_continue():
    #ask user if they're ready to continue
    question_continue = input(f"""{Fore.GREEN}
Take your time and let me know when you're ready 
to continue.\n
Please type "continue".
{Style.RESET_ALL}""")
    
    #if continue, print string and go to positive affirmations
    if question_continue ==("continue"):
        print(f"""{Fore.GREEN}
Well done! Taking a moment to ground yourself 
can be so powerful.
{Style.RESET_ALL}""")
        time.sleep(3)
        ask_positive_affirmations()

    #if other response, give user the options 
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type “continue” when you’re ready to move on.
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_continue()






def ask_grounding():
    #ask user to start or skip grounding exercise
    intro_grounding =(f"""{Fore.GREEN}
Let’s try something a bit different instead. 

We’ll move on to a grounding exercise that can 
help bring you into the present moment and find 
a sense of calm. 
                      
There is no pressure! You will have time to finish 
the exercise before moving on. If you feel more 
comfortable, wait until I finish naming all the steps.
{Style.RESET_ALL}""")
    
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
        ask_continue()

    #if skip, go to positive affirmations
    elif question_grounding_start == ("skip"):
        ask_positive_affirmations()

    #if other response, give user the options 
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “start” or “skip.”
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_grounding()






def ask_breathing_repeat(classifier):
    #ask user if they wanna repeat exercise
    print(f"""{Fore.GREEN} 
If you'd like, we can try the breathing exercise again 
to help bring you some calm. 
{Style.RESET_ALL}""")

    time.sleep(2) #pause

    question_repeat = input(f"""{Fore.GREEN}          
Would you be interested?\n
{Style.RESET_ALL}""")

    
    #if yes, repeat breathing exercise
    if question_repeat.lower() == "yes":
        ask_breathing2(classifier)

    #if no, move on to grounding exercise
    elif question_repeat.lower() == "no":
        print(f"""{Fore.GREEN}
That's perfectly ok!
{Style.RESET_ALL}""")
        time.sleep(1)#pause
        ask_grounding()

    #if other response, give user the options 
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “yes” or “no.”
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_breathing_repeat(classifier)




classifier = Feelings() #instance of class Feelings

def ask_breathing2(classifier):
    #explaining breathing exrcise to user
    question_breathing_start = input(f"""{Fore.GREEN}                          
Shall we start? Type “start” when you are ready.\n
{Style.RESET_ALL}""")
    
    #if start, begin breathing exercise
    if question_breathing_start.lower() == "start":
        breathing = BreathingExercise(breath_count=4, repeat_count=3, delay=1)
        breathing.perform() #start breathing exercise
        print(f"""{Fore.GREEN}
Well done! Breathing can be a great way to bring focus 
to the body while emptying your mind. 
{Style.RESET_ALL}""")
        time.sleep(2)
        question_feeling_breathing = input(f"""{Fore.GREEN}                                 
How are you feeling right now?\n
{Style.RESET_ALL}""") 
        
        sentiment = classifier.classify(question_feeling_breathing) # classify user's response according to what they're feeling

        if sentiment == 'negative':
            print(f"{Fore.GREEN}It's okay to feel this way, and it will get better.{Style.RESET_ALL}")
        elif sentiment == 'neutral':
            print(f"{Fore.GREEN}Got it. Thank you for sharing that with me.{Style.RESET_ALL}")
        elif sentiment == 'positive':
            print(f"{Fore.GREEN}It’s great that you’re feeling good!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Hmm, feelings can be confusing... {Style.RESET_ALL}")

        time.sleep(3)#pause
        ask_breathing_repeat(classifier)# start repetition question

    #if other response, give user the reply options
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type “start” when you're ready to begin the exercise.
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_breathing2(classifier)






def ask_breathing_1(classifier):
    #ask user for permission to start breathing exercise and give them a health discloser
    question_breathing_skip = input(f"""{Fore.GREEN}
Do you wish to start?                                    
Please type “yes” or “skip”.\n
{Style.RESET_ALL}""")

    #if yes, go to explaining the breathing exercise
    if question_breathing_skip.lower() == "yes":
       print(f"""
{Fore.GREEN}Wonderful!{Style.RESET_ALL}
""")
       time.sleep(1) #add pause and move on to exercise explanation
       ex_explanation = (f"""{Fore.GREEN}
Let’s do the 4-4-4 exercise. 
                                     
You’re going to take a deep breath in for 4 counts, 
hold for 4 counts and exhale for 4 counts. 

I will take care of the counts so you can just seat back and relax. 
{Style.RESET_ALL}""")
       
       displayer = TextPauses(ex_explanation)
       displayer.display()

       ask_breathing2(classifier)

    #if skip, move on to grounding exrcise
    elif question_breathing_skip.lower() == "skip":
        ask_grounding()

    #if other response, give user the reply options
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “yes” or “skip”.
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        ask_breathing_1(classifier)






def start_convo(classifier):
    #the convo goes from text_start to here. User interaction begins
    question_start = input(f"""{Fore.GREEN}
Shall we get started?\n
Please type "yes" or "no"        
{Style.RESET_ALL}""")

    #if yes, user goes to breathing exercises
    if question_start.lower() == "yes":
        print(f"""
{Fore.GREEN}Lovely!{Style.RESET_ALL}
""")
        time.sleep(1) #Pause
        breathing_ex_question = f"""
{Fore.GREEN}
Would you like to try a breathing exercise, 
or perhaps explore a different calming approach 
that feels right for you? 
                                    
Note: Please don’t attempt this exercise if you 
have breathing problems or any conditions that 
may get worsen by this exercise.
{Style.RESET_ALL}"""
        
        displayer = TextPauses(breathing_ex_question) #adds pauses between paragraphs
        displayer.display()

        ask_breathing_1(classifier)

    #if no, exit 
    elif question_start.lower() == "no":
        text_exit = f"""{Fore.GREEN}
That is alright. If you change your mind and 
want to give in to relaxation, I am a push of 
a button away. Hope to see you soon.
{Style.RESET_ALL}"""
        print(text_exit)
        exit()

    #if other response, give user the reply options
    else:
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “yes” or “no.”
{Style.RESET_ALL}""")
        
        time.sleep(2)#pause before asking again
        start_convo(classifier)


start_convo(classifier)
