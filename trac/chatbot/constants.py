from colorama import Fore, Style

# === General UI Strings ===
RETRY_YES_NO = f"{Fore.GREEN}Apologies but I did not understand. Please type either 'yes' or 'no'.{Style.RESET_ALL}"
RETRY_YES_SKIP = f"{Fore.GREEN}Apologies but I did not understand. Please type 'yes' or 'skip'.{Style.RESET_ALL}"
RETRY_START = f"{Fore.GREEN}Apologies but I did not understand. Please type 'start' when you're ready to begin the exercise.{Style.RESET_ALL}"
RETRY_START_SKIP = f"{Fore.GREEN}Apologies but I did not understand. Please type either 'start' or 'skip'.{Style.RESET_ALL}"
RETRY_CONTINUE = f"{Fore.GREEN}Apologies but I did not understand. Please type 'continue' when you’re ready to move on.{Style.RESET_ALL}"
RETRY_CAFE_PROMPT = f"{Fore.GREEN}Apologies but I did not understand. Please type either 'yes' or 'conclude'.{Style.RESET_ALL}"
RETRY_AFFIRMATION_CHOICE = f"{Fore.GREEN}Apologies but I did not understand. Please type '1', '2', '3' or '4'.{Style.RESET_ALL}"

# === Intro ===
INTRO_TEXT = f"""{Fore.GREEN}
Hello, I’m TRAC, your Tranquility, Reflection and Awareness Chatbot.
I’m here to help you find moments of calm and clarity.
Whether you’re feeling overwhelmed or just need to unwind a bit, these strategies can be a great way to restore balance.
{Style.RESET_ALL}"""
QUESTION_START = f"{Fore.GREEN}Shall we get started? Please type 'yes' or 'no'.\n{Style.RESET_ALL}"
EXIT_MESSAGE = f"{Fore.GREEN}That is alright. If you change your mind and want to give in to relaxation, I am a push of a button away. Hope to see you soon.{Style.RESET_ALL}"

# === Breathing ===
BREATHING_INTRO = f"{Fore.GREEN}Would you like to try a breathing exercise, or perhaps explore a different calming approach that feels right for you?\nNote: Please don’t attempt this exercise if you have breathing problems or any conditions that may worsen by this exercise.{Style.RESET_ALL}"
QUESTION_BREATHING_1 = f"{Fore.GREEN}Do you wish to start? Please type 'yes' or 'skip'.\n{Style.RESET_ALL}"
POSITIVE_ACK = f"{Fore.GREEN}Wonderful!{Style.RESET_ALL}\n"
BREATHING_DETAILS = f"{Fore.GREEN}Let’s do the 4-4-4 exercise.\nYou’re going to take a deep breath in for 4 counts, hold for 4 counts and exhale for 4 counts.\nI will take care of the counts so you can just sit back and relax.{Style.RESET_ALL}"
QUESTION_BREATHING_START = f"{Fore.GREEN}Shall we start? Type 'start' when you are ready.\n{Style.RESET_ALL}"
AFTER_BREATHING_MSG = f"{Fore.GREEN}Well done! Breathing can be a great way to bring focus to the body while emptying your mind.{Style.RESET_ALL}"
QUESTION_FEELING_AFTER_BREATHING = f"{Fore.GREEN}How are you feeling right now?\n{Style.RESET_ALL}"
REPEAT_BREATHING_PROMPT = f"{Fore.GREEN}If you'd like, we can try the breathing exercise again to help bring you some calm.{Style.RESET_ALL}"
REPEAT_BREATHING_Q = f"{Fore.GREEN}Would you be interested?\n{Style.RESET_ALL}"
ACK_NO_REPEAT = f"{Fore.GREEN}That's perfectly ok!{Style.RESET_ALL}"
RESPONSES_SENTIMENT = {
    "negative": f"{Fore.GREEN}It's okay to feel this way, and it will get better.{Style.RESET_ALL}",
    "neutral": f"{Fore.GREEN}Got it. Thank you for sharing that with me.{Style.RESET_ALL}",
    "positive": f"{Fore.GREEN}It’s great that you’re feeling good!{Style.RESET_ALL}",
    "default": f"{Fore.GREEN}Hmm, feelings can be confusing...{Style.RESET_ALL}"
}

# === Grounding ===
GROUNDING_INTRO = f"{Fore.GREEN}Let’s try something a bit different instead.\nWe’ll move on to a grounding exercise that can help bring you into the present moment and find a sense of calm.\nThere is no pressure! You will have time to finish the exercise before moving on. If you feel more comfortable, wait until I finish naming all the steps.{Style.RESET_ALL}"
GROUNDING_PROMPT = f"{Fore.GREEN}Please type 'start' or 'skip'.\n{Style.RESET_ALL}"
GROUNDING_EXERCISE = f"{Fore.GREEN}Let’s try a grounding exercise called “5-4-3-2-1.”\nThis helps bring you to the present moment.\n- Name 5 things you can see around you.\n- Name 4 things you can touch.\n- Name 3 things you can hear.\n- Name 2 things you can smell.\n- And finally, name 1 thing you can taste.{Style.RESET_ALL}"

# === Continue Prompt ===
CONTINUE_PROMPT = f"{Fore.GREEN}Take your time and let me know when you're ready to continue.\nPlease type 'continue'.{Style.RESET_ALL}"
CONTINUE_ACK = f"{Fore.GREEN}Well done! Taking a moment to ground yourself can be so powerful.{Style.RESET_ALL}"

# === Affirmations ===
POSITIVE_INTRO = f"{Fore.GREEN}Now, let’s continue with some positive affirmations to uplift and encourage you. These can be a wonderful way to reinforce a sense of confidence.{Style.RESET_ALL}"
AFFIRMATIONS_START_PROMPT = f"{Fore.GREEN}Ready to give it a try? Please type 'start' or 'skip'.\n{Style.RESET_ALL}"
AFFIRMATIONS_LIST = f"{Fore.GREEN}Here are a few affirmations for today. Repeat each one slowly to yourself, or let me know which resonates most:\n1 - “I am worthy of peace and calm.”\n2 - “I am doing my best, and that’s enough.”\n3 - “I am resilient, strong, and capable.”\n4 - “I trust myself to handle what comes my way.”{Style.RESET_ALL}"
AFFIRMATION_CHOICE_PROMPT = f"{Fore.GREEN}Which one speaks to you most? Phrase 1, 2, 3 or 4?\n{Style.RESET_ALL}"
AFFIRMATION_RESPONSES = {
    "1": f"{Fore.GREEN}Absolutely, you deserve all the peace and calm that life has to offer. Embracing that worthiness can be so empowering.{Style.RESET_ALL}",
    "2": f"{Fore.GREEN}That’s a beautiful reminder. Your best is more than enough, and honoring that can bring such a sense of relief.{Style.RESET_ALL}",
    "3": f"{Fore.GREEN}Yes! You have such strength within you. Remembering this can help you face any challenge that comes your way.{Style.RESET_ALL}",
    "4": f"{Fore.GREEN}Trusting yourself is so powerful. You’re capable and resilient, ready to face whatever comes.{Style.RESET_ALL}"
}
POSITIVE_REINFORCEMENT = f"{Fore.GREEN}Great job! Taking a moment to connect with yourself like this is a wonderful step.{Style.RESET_ALL}"
CAFE_INTRO = f"{Fore.GREEN}Now that we’ve set a positive foundation, let’s explore some cozy cafes where you can relax, reflect, or simply enjoy a peaceful moment.{Style.RESET_ALL}"
CAFE_PRIVACY_NOTE = f"{Fore.GREEN}Quick note: our cafe recommendations use a location-based search to find calming spots nearby, but rest assured, your location information is only used temporarily for this purpose and isn’t stored. Your privacy and confidentiality are always protected. Also, this task requires wifi connection.{Style.RESET_ALL}"

# === Cafe Flow ===
CAFE_PROMPT = f"{Fore.GREEN}Ready to find a cozy spot? Please type 'yes' or 'conclude'.\n{Style.RESET_ALL}"
CAFE_FOUND = f"{Fore.GREEN}\nI hope you found a cafe that piqued your interest!{Style.RESET_ALL}"
CAFE_NOT_FOUND = f"{Fore.GREEN}\nI'm sorry I couldn't find any cafes nearby.{Style.RESET_ALL}"
CAFE_CONCLUDE_TEXT = f"{Fore.GREEN}Thank you for spending this time with me today.\nI hope the techniques we explored bring you some calm and comfort.{Style.RESET_ALL}"

# === Cafe Logic ===
ENTER_POSTAL_CODE = f"{Fore.GREEN}Please enter your postal code: {Style.RESET_ALL}"
ENTER_RADIUS = f"{Fore.GREEN}Enter the search radius in miles (numbers only): {Style.RESET_ALL}"
INVALID_RADIUS_INPUT = f"{Fore.GREEN}Invalid input for radius. Please enter a valid number.{Style.RESET_ALL}"
INVALID_POSTAL_CODE = f"{Fore.GREEN}Invalid postal code. Please try again.{Style.RESET_ALL}"
LOCATION_NOT_FOUND = f"{Fore.GREEN}Could not find location for postal code: {{}}{Style.RESET_ALL}"
LOCATION_ERROR = f"{Fore.GREEN}Error occurred while fetching location: {{}}{Style.RESET_ALL}"
NO_CAFES_IN_RADIUS = f"{Fore.GREEN}No nearby cafes found within the given radius.{Style.RESET_ALL}"
CAFES_WITHIN_RADIUS = f"{Fore.GREEN}\nNearby cafes within {{}} miles (max {{}} results):{Style.RESET_ALL}"
CAFE_INFO = f"{Fore.GREEN}{{}} ({{:.2f}} miles){Style.RESET_ALL}"
NO_NAMED_CAFES = f"{Fore.GREEN}No cafes with a name found in the given radius.{Style.RESET_ALL}"
CAFE_FETCH_ERROR = f"{Fore.GREEN}Error: Unable to fetch nearby cafes. Details: {{}}{Style.RESET_ALL}"

# === Conclusion ===
CONCLUSION_PROMPT = f"{Fore.GREEN}Before we wrap up, I’d love to hear—how are you feeling after our session?\n{Style.RESET_ALL}"
CONCLUSION_GENERIC_RESPONSE = f"{Fore.GREEN}It sounds like there’s a lot on your mind.{Style.RESET_ALL}"
CLOSING_RECOMMENDATIONS = f"{Fore.GREEN}Before we part, here are a few small ways to carry calm with you throughout the day:\n\n- Pause for a few deep breaths whenever things feel overwhelming.\n- Take a brief walk outside or find a quiet corner to unwind.\n- Practice gratitude by naming one thing you’re thankful for today.\n\nRemember, it’s okay to take breaks and prioritize your well-being. Little moments of care make a big difference.{Style.RESET_ALL}"
FINAL_GOODBYE = f"{Fore.GREEN}Thank you for being here, and remember, I’m always just a message away if you need a moment of calm.{Style.RESET_ALL}"
