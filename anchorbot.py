from chatbot_base import ChatbotBase

# Standard library
import time
import re

# Third-party libraries
import requests
from colorama import Fore, Style
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is available for sentiment analysis
nltk.download('vader_lexicon')


class MyChatbot(ChatbotBase):
    """
    A chatbot class extending the base chatbot.
    Currently a placeholder for future extension.
    """
    def __init__(self, name="Chatbot"):
        super().__init__(name)


# Final iteration note
text_explain = "Last few changes after feedback."


class TextPauses:
    """
    Displays multi-paragraph text with pauses between paragraphs.

    This improves readability when printing long text by pausing 
    after each paragraph or block of text.

    Args:
        text (str): The full text to display.
        pause (int): Number of seconds to pause between paragraphs.
    """
    def __init__(self, text, pause=5):
        self.text = text
        self.pause = pause

    def display(self):
        """
        Prints the text to the console with a pause between paragraphs.

        Splits the text by blank lines, prints each paragraph, then pauses.
        """
        # Split text on blank lines (paragraph separators)
        sections = re.split(r'(\n\s*\n)', self.text)
        for section in sections:
            if section.strip():
                print(section.strip())
                time.sleep(self.pause)
            else:
                print("")  # Print blank line to preserve paragraph spacing


class BreathingExercise:
    """
    Guides the user through a structured breathing exercise with timed counts.

    The exercise consists of multiple cycles where the user breathes in, holds,
    and breathes out for a fixed number of counts.

    Args:
        breath_count (int): Number of seconds/counts per breathing phase.
        repeat_count (int): Number of cycles to repeat the breathing phases.
        delay (float): Time in seconds between each count print.
    """
    def __init__(self, breath_count=4, repeat_count=3, delay=1):
        self.breath_count = breath_count
        self.repeat_count = repeat_count
        self.delay = delay

    def count_down(self, phase):
        """
        Performs a countdown for a given breathing phase.

        Args:
            phase (str): Name of the breathing phase, e.g., "Breathing in..."
        """
        print(f"{Fore.GREEN}{phase}{Style.RESET_ALL}")
        for i in range(self.breath_count, 0, -1):
            print(f"{Fore.GREEN}{i}{Style.RESET_ALL}")
            time.sleep(self.delay)

    def perform(self):
        """
        Runs the full breathing exercise consisting of multiple cycles.

        Each cycle includes:
        - Breathing in
        - Holding breath
        - Breathing out

        Pauses briefly between cycles.
        """
        for cycle in range(1, self.repeat_count + 1):
            print(f"\n{Fore.GREEN}Cycle {cycle} of {self.repeat_count}{Style.RESET_ALL}")
            self.count_down("Breathing in...")
            self.count_down("Holding...")
            self.count_down("Breathing out...")
            time.sleep(1)  # Short pause between cycles


class CafeLogic:
    """
    Handles geolocation lookup and nearby cafe search using Nominatim and Overpass API.

    Provides methods to:
    - Convert postal codes to geographic coordinates.
    - Query OpenStreetMap for cafes near a location within a given radius.
    - Display cafe names and distances to the user.

    Args:
        max_results (int): Maximum number of cafe results to display.
        user_agent (str): User agent string for geopy's Nominatim service.
    """
    def __init__(self, max_results=20, user_agent="location_lookup"):
        self.max_results = max_results
        self.geolocator = Nominatim(user_agent=user_agent)

    def get_location_from_postal_code(self, postal_code):
        """
        Converts a postal code string into latitude and longitude coordinates.

        Args:
            postal_code (str): The postal code or address to geocode.

        Returns:
            tuple: (latitude, longitude) if found; otherwise (None, None).
        """
        try:
            location = self.geolocator.geocode(postal_code)
            if location:
                return location.latitude, location.longitude
            print(Fore.GREEN + f"Could not find location for postal code: {postal_code}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.GREEN + f"Error occurred while fetching location: {e}" + Style.RESET_ALL)
        return None, None

    def find_nearby_cafes(self, lat, lon, radius):
        """
        Queries OpenStreetMap Overpass API for cafes within a given radius around lat/lon.

        Args:
            lat (float): Latitude of the search center.
            lon (float): Longitude of the search center.
            radius (float): Search radius in miles.

        Returns:
            bool: True if cafes found and printed; False otherwise.
        """
        overpass_url = "http://overpass-api.de/api/interpreter"
        osm_tag = "amenity=cafe"

        # Convert miles to meters for Overpass API radius
        radius_meters = int(radius * 1609.34)

        query = f"""
        [out:json];
        node[{osm_tag}]
          (around:{radius_meters},{lat},{lon});
        out;
        """

        try:
            response = requests.get(overpass_url, params={'data': query})
            response.raise_for_status()
            data = response.json()

            cafes_found = 0
            elements = data.get('elements', [])

            if not elements:
                print(Fore.GREEN + "No nearby cafes found within the given radius." + Style.RESET_ALL)
                return False

            print(Fore.GREEN + f"\nNearby cafes within {radius} miles (max {self.max_results} results):" + Style.RESET_ALL)

            for element in elements:
                if cafes_found >= self.max_results:
                    break

                place_lat = element.get('lat')
                place_lon = element.get('lon')
                place_name = element.get('tags', {}).get('name')

                if place_name and place_lat and place_lon:
                    # Calculate distance in miles for user friendliness
                    distance_km = geodesic((lat, lon), (place_lat, place_lon)).kilometers
                    distance_miles = distance_km * 0.621371
                    print(Fore.GREEN + f"{place_name} ({distance_miles:.2f} miles)" + Style.RESET_ALL)
                    cafes_found += 1

            if cafes_found == 0:
                print(Fore.GREEN + "No cafes with a name found in the given radius." + Style.RESET_ALL)
                return False

            return True

        except requests.RequestException as e:
            print(Fore.GREEN + f"Error: Unable to fetch nearby cafes. Details: {e}" + Style.RESET_ALL)
            return False

    def run(self):
        """
        Runs an interactive loop prompting the user for a postal code and search radius.

        Uses the postal code to find coordinates and then searches for cafes nearby.

        Loops until valid inputs are provided and results are found.
        """
        while True:
            postal_code = input(f"{Fore.GREEN}Please enter your postal code: {Style.RESET_ALL}")
            lat, lon = self.get_location_from_postal_code(postal_code)

            if lat is not None and lon is not None:
                try:
                    search_radius = float(input(f"{Fore.GREEN}Enter the search radius in miles (numbers only): {Style.RESET_ALL}"))
                    results_found = self.find_nearby_cafes(lat, lon, search_radius)
                    return results_found
                except ValueError:
                    print(Fore.GREEN + "Invalid input for radius. Please enter a valid number." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "Invalid postal code. Please try again." + Style.RESET_ALL)


class Feelings:
    """
    Uses NLTK's VADER sentiment analysis to classify text sentiment.

    The sentiment is categorized into:
    - 'positive'
    - 'neutral'
    - 'negative'
    based on the compound sentiment score.
    """
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def classify(self, text):
        """
        Classify the sentiment of the given text input.

        Args:
            text (str): User input text to classify.

        Returns:
            str: Sentiment category ('positive', 'neutral', 'negative').
        """
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound < -0.5:
            return 'negative'
        elif compound > 0.5:
            return 'positive'
        else:
            return 'neutral'


# === Intro Message ===
# This text introduces the chatbot and its purpose using green colored text for calmness
text = f"""{Fore.GREEN}
Hello, I’m TRAC, your Tranquility, Reflection and 
Awareness Chatbot.

I’m here to help you find moments of calm and clarity.

Whether you’re feeling overwhelmed or just need to 
unwind a bit, these strategies can be a great way to 
restore balance.
{Style.RESET_ALL}"""

# Split the intro text into sections based on blank lines to create pauses
sections = re.split(r'(\n\s*\n)', text)

# Loop through each section and print it with a pause for better pacing and readability
for section in sections:
    if section.strip():
        print(section.strip())  # print non-empty sections (paragraphs)
        time.sleep(3)  # pause 3 seconds between paragraphs
    else:
        print("")  # print blank lines as is to keep formatting
time.sleep(1)  # final pause before moving on


# === Conclusion Question Function ===
def ask_conclusion(classifier):
    # Ask the user how they feel after the session, with green text prompt
    question_conclusion_feel = input(f"""{Fore.GREEN}
Before we wrap up, I’d love to hear—
how are you feeling after our session?
\n{Style.RESET_ALL}""")

    # Use the classifier instance to detect the sentiment of the user's response
    sentiment = classifier.classify(question_conclusion_feel)

    # Respond empathetically based on the detected sentiment
    if sentiment == 'negative':
        print(f"{Fore.GREEN}It’s okay to not be okay right now.{Style.RESET_ALL}")
    elif sentiment == 'neutral':
        print(f"{Fore.GREEN}I appreciate you telling me that.{Style.RESET_ALL}")
    elif sentiment == 'positive':
        print(f"{Fore.GREEN}That's wonderful to hear!{Style.RESET_ALL}")
    else:
        # Fallback message if sentiment can't be determined
        print(f"{Fore.GREEN}It sounds like there’s a lot on your mind.{Style.RESET_ALL}")

    time.sleep(3)

    # Prepare closing recommendations to carry calm throughout the day
    recommendations = f"""{Fore.GREEN}
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
{Style.RESET_ALL}"""

    # Use a helper class TextPauses to display text with pauses for soothing effect
    displayer = TextPauses(recommendations)
    displayer.display()

    # Final thank you message and gentle reminder that chatbot is always available
    print(f"""{Fore.GREEN}
Thank you for being here, and remember, I’m always just a 
message away if you need a moment of calm.
{Style.RESET_ALL}""")

    time.sleep(2)
    exit()  # End the program after conclusion


# === Cafe Prompt Function ===
def ask_cafe():
    # Text shown if user chooses to conclude without cafe suggestions
    text_conclusion = f"""{Fore.GREEN}
Thank you for spending this time with me today.

I hope the techniques we explored—whether affirmations, 
breathing exercises, or recommendations—bring you some 
calm and comfort.
{Style.RESET_ALL}"""

    # Ask user if they want to find a cozy cafe or conclude the session
    question_start_cafe = input(f"""{Fore.GREEN}
Ready to find a cozy spot? 
Please type “yes” or “conclude”.
\n{Style.RESET_ALL}""").strip().lower()

    if question_start_cafe == "yes":
        # If yes, create an instance of CafeLogic to find cafes nearby
        chatbot = CafeLogic()
        results_found = chatbot.run()
        time.sleep(3)

        # Give feedback based on whether any cafes were found
        if results_found:
            print(f"{Fore.GREEN}\nI hope you found a cafe that piqued your interest!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}\nI'm sorry I couldn't find any cafes nearby.{Style.RESET_ALL}")

        time.sleep(3)
        ask_conclusion(classifier)  # proceed to conclusion questions

    elif question_start_cafe == "conclude":
        # If user chooses to conclude, display closing text with pauses
        displayer = TextPauses(text_conclusion)
        displayer.display()
        ask_conclusion(classifier)

    else:
        # If input is not recognized, ask again with a polite prompt
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “yes” or “conclude.”
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_cafe()  # recursive call to retry input


# === Feeling Affirmations Function ===
def ask_feeling_affirmations():
    # Text offering positive reinforcement after user picks an affirmation phrase
    text_positive_reinforcement = f"""{Fore.GREEN}
Great job! Taking a moment to connect with yourself 
like this is a wonderful step.
{Style.RESET_ALL}"""

    # Text introducing cafes after affirmations
    text_cafe = f"""{Fore.GREEN}
Now that we’ve set a positive foundation, let’s 
explore some cozy cafes where you can relax, 
reflect, or simply enjoy a peaceful moment.
{Style.RESET_ALL}"""

    # Privacy disclaimer about location usage for cafe recommendations
    text_permission = f"""{Fore.GREEN}
Quick note: our cafe recommendations use a
location-based search to find calming spots
nearby, but rest assured, your location information
is only used temporarily for this purpose and isn’t
stored. Your privacy and confidentiality are always
protected. Also, this task requires wifi connection.
{Style.RESET_ALL}"""

    # Prompt user to pick their favorite phrase from options 1 to 4
    question = input(f"{Fore.GREEN}Which one speaks to you most? Phrase 1, 2, 3 or 4?\n{Style.RESET_ALL}").strip()

    # Dictionary mapping user choices to affirmation responses
    responses = {
        "1": f"""{Fore.GREEN}
Absolutely, you deserve all the peace and calm 
that life has to offer. Embracing that worthiness 
can be so empowering.
{Style.RESET_ALL}""",
        "2": f"""{Fore.GREEN}
That’s a beautiful reminder. Your best is more 
than enough, and honoring that can bring such 
a sense of relief.
{Style.RESET_ALL}""",
        "3": f"""{Fore.GREEN}
Yes! You have such strength within you. 
Remembering this can help you face any challenge 
that comes your way.
{Style.RESET_ALL}""",
        "4": f"""{Fore.GREEN}
Trusting yourself is so powerful. You’re capable and 
resilient, ready to face whatever comes.
{Style.RESET_ALL}"""
    }

    # Check if user input matches one of the keys and respond accordingly
    if question in responses:
        print(responses[question])
        time.sleep(4)
        print(text_positive_reinforcement)
        time.sleep(3)
        print(text_cafe)
        time.sleep(5)
        print(text_permission)
        time.sleep(10)
        ask_cafe()  # move on to cafe prompt
    else:
        # Handle invalid input by asking again
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type “1”, “2”, “3” or “4”.
{Style.RESET_ALL}""")
        time.sleep(3)
        ask_feeling_affirmations()  # recursive retry


# === Positive Affirmations Function ===
def ask_positive_affirmations():
    # Introduce affirmations to uplift and encourage the user
    print(f"""{Fore.GREEN}
Now, let’s continue with some positive affirmations 
to uplift and encourage you. These can be a wonderful 
way to reinforce a sense of confidence. 
{Style.RESET_ALL}""")
    
    time.sleep(4)

    # Ask user if they want to start the affirmations or skip
    choice = input(f"""{Fore.GREEN}
Ready to give it a try?
Please type “start” or “skip”.\n
{Style.RESET_ALL}""").strip().lower()

    if choice == "start":
        # Affirmations text with four options for user to choose from
        affirmations_list = f"""{Fore.GREEN}
Here are a few affirmations for today. Repeat each one
slowly to yourself, or let me know which resonates most:
              
1 - “I am worthy of peace and calm.”
                             
2 - “I am doing my best, and that’s enough.”
                             
3 - “I am resilient, strong, and capable.”
                             
4 - “I trust myself to handle what comes my way.”
{Style.RESET_ALL}"""
        
        # Display affirmations with pauses for calm reading
        displayer = TextPauses(affirmations_list)
        displayer.display()

        # Move on to ask user which affirmation they prefer
        ask_feeling_affirmations()

    elif choice == "skip":
        # Skip affirmations and move directly to cafe prompt
        ask_cafe()

    else:
        # Handle invalid input with a polite retry prompt
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either “start” or “skip.”
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_positive_affirmations()  # recursive retry


# === Continue Prompt Function ===
def ask_continue():
    """Prompt user to type 'continue' to proceed with grounding exercise."""

    question_continue = input(f"""{Fore.GREEN}
Take your time and let me know when you're ready 
to continue.

Please type "continue".
{Style.RESET_ALL}""")

    # If user types 'continue', proceed to positive affirmations
    if question_continue == "continue":
        print(f"""{Fore.GREEN}
Well done! Taking a moment to ground yourself 
can be so powerful.
{Style.RESET_ALL}""")
        time.sleep(3)
        ask_positive_affirmations()
    else:
        # Otherwise, politely ask again until user types 'continue'
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type "continue" when you’re ready to move on.
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_continue()  # recursive retry


# === Grounding Exercise Prompt Function ===
def ask_grounding():
    """Offer user a grounding exercise or allow them to skip it."""

    # Introductory message explaining grounding exercise and no pressure to rush
    intro_grounding = f"""{Fore.GREEN}
Let’s try something a bit different instead. 

We’ll move on to a grounding exercise that can 
help bring you into the present moment and find 
a sense of calm. 
                  
There is no pressure! You will have time to finish 
the exercise before moving on. If you feel more 
comfortable, wait until I finish naming all the steps.
{Style.RESET_ALL}"""

    # Display the introductory message with pauses for better pacing
    displayer = TextPauses(intro_grounding)
    displayer.display()

    # Ask if user wants to start the grounding exercise or skip it
    question = input(f"""{Fore.GREEN}
Please type "start" or "skip".

{Style.RESET_ALL}""")

    if question == "start":
        # Description of the 5-4-3-2-1 grounding exercise steps
        grounding_ex = f"""{Fore.GREEN}
Let’s try a grounding exercise called “5-4-3-2-1.” 
This helps bring you to the present moment.
              
- Name **5 things** you can see around you. 
                    
- Name **4 things** you can touch. 
                    
- Name **3 things** you can hear. 
                    
- Name **2 things** you can smell. 
                    
- And finally, name **1 thing** you can taste. 
{Style.RESET_ALL}"""

        # Display grounding exercise instructions with pauses
        displayer = TextPauses(grounding_ex)
        displayer.display()
        ask_continue()  # prompt to continue after exercise

    elif question == "skip":
        # Skip grounding exercise and move on to positive affirmations
        ask_positive_affirmations()
    else:
        # Handle invalid input and retry prompt
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either "start" or "skip."
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_grounding()  # recursive retry


# === Breathing Exercise Repeat Prompt Function ===
def ask_breathing_repeat(classifier):
    """Ask user if they want to repeat the breathing exercise for extra calm."""

    print(f"""{Fore.GREEN}
If you'd like, we can try the breathing exercise again 
to help bring you some calm. 
{Style.RESET_ALL}""")
    time.sleep(2)

    # Prompt for yes or no response
    question_repeat = input(f"""{Fore.GREEN}
Would you be interested?
{Fore.RESET}""").strip().lower()

    if question_repeat == "yes":
        # If yes, repeat the breathing exercise function
        ask_breathing2(classifier)
    elif question_repeat == "no":
        # If no, acknowledge and move to grounding exercise
        print(f"""{Fore.GREEN}
That's perfectly ok!
{Style.RESET_ALL}""")
        time.sleep(1)
        ask_grounding()
    else:
        # Handle unrecognized input and retry
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either "yes" or "no."
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_breathing_repeat(classifier)


# Create an instance of the Feelings classifier to be used for sentiment analysis
classifier = Feelings()  


def ask_breathing2(classifier):
    """Guide the user through the breathing exercise."""

    # Prompt user to start the breathing exercise
    question_breathing_start = input(f"""{Fore.GREEN}
Shall we start? Type "start" when you are ready.

{Style.RESET_ALL}""").strip().lower()

    if question_breathing_start == "start":
        # Create and perform breathing exercise instance with specified parameters
        breathing = BreathingExercise(breath_count=4, repeat_count=3, delay=1)
        breathing.perform()

        print(f"""{Fore.GREEN}
Well done! Breathing can be a great way to bring focus 
to the body while emptying your mind. 
{Style.RESET_ALL}""")
        time.sleep(2)

        # Ask user how they feel after the exercise
        feeling_input = input(f"""{Fore.GREEN}
How are you feeling right now?

{Style.RESET_ALL}""")
        # Use classifier to determine sentiment of the user's input
        sentiment = classifier.classify(feeling_input)

        # Respond based on classified sentiment
        if sentiment == "negative":
            print(f"{Fore.GREEN}It's okay to feel this way, and it will get better.{Style.RESET_ALL}")
        elif sentiment == "neutral":
            print(f"{Fore.GREEN}Got it. Thank you for sharing that with me.{Style.RESET_ALL}")
        elif sentiment == "positive":
            print(f"{Fore.GREEN}It’s great that you’re feeling good!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Hmm, feelings can be confusing... {Style.RESET_ALL}")

        time.sleep(3)
        # Ask if user wants to repeat the breathing exercise
        ask_breathing_repeat(classifier)

    else:
        # Handle invalid input by prompting again
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type "start" when you're ready to begin the exercise.
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_breathing2(classifier)


def ask_breathing_1(classifier):
    """Ask user permission to start breathing exercise, including a health disclaimer."""

    question = input(f"""{Fore.GREEN}
Do you wish to start?                                  
Please type "yes" or "skip".

{Style.RESET_ALL}""").strip().lower()

    if question == "yes":
        print(f"{Fore.GREEN}Wonderful!{Style.RESET_ALL}\n")
        time.sleep(1)

        explanation = f"""{Fore.GREEN}
Let’s do the 4-4-4 exercise. 

You’re going to take a deep breath in for 4 counts, 
hold for 4 counts and exhale for 4 counts. 

I will take care of the counts so you can just sit back and relax. 
{Style.RESET_ALL}"""

        # Display explanation with pauses for better readability
        displayer = TextPauses(explanation)
        displayer.display()

        # Proceed to actual breathing exercise
        ask_breathing2(classifier)

    elif question == "skip":
        # If user skips, offer alternative grounding exercise
        ask_grounding()

    else:
        # Handle invalid input by prompting again
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either "yes" or "skip".
{Style.RESET_ALL}""")
        time.sleep(2)
        ask_breathing_1(classifier)


def start_convo(classifier):
    """Start conversation; ask user if they want to begin and guide them through options."""

    question = input(f"""{Fore.GREEN}
Shall we get started?
Please type "yes" or "no".

{Style.RESET_ALL}""").strip().lower()

    if question == "yes":
        print(f"{Fore.GREEN}Lovely!{Style.RESET_ALL}\n")
        time.sleep(1)

        breathing_explanation = f"""{Fore.GREEN}
Would you like to try a breathing exercise, 
or perhaps explore a different calming approach 
that feels right for you? 

Note: Please don’t attempt this exercise if you 
have breathing problems or any conditions that 
may worsen by this exercise.
{Style.RESET_ALL}"""

        # Show explanation with pauses
        displayer = TextPauses(breathing_explanation)
        displayer.display()

        # Ask for permission to start breathing exercise
        ask_breathing_1(classifier)

    elif question == "no":
        # Exit politely if user declines to start
        exit_message = f"""{Fore.GREEN}
That is alright. If you change your mind and 
want to give in to relaxation, I am a push of 
a button away. Hope to see you soon.
{Style.RESET_ALL}"""
        print(exit_message)
        exit()

    else:
        # Handle invalid input by prompting again
        print(f"""{Fore.GREEN}
Apologies but I did not understand. 
Please type either "yes" or "no."
{Style.RESET_ALL}""")
        time.sleep(2)
        start_convo(classifier)


# Start the conversation by calling start_convo with the classifier instance
start_convo(classifier)
