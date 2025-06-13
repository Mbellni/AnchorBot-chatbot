from colorama import Fore, Style

INTRO_TEXT = f"""{Fore.GREEN}
Hello, I’m TRAC, your Tranquility, Reflection and Awareness Chatbot...
{Style.RESET_ALL}"""

QUESTION_START = f"{Fore.GREEN}Shall we get started? Type 'yes' or 'no'.\n{Style.RESET_ALL}"
EXIT_MESSAGE = f"{Fore.GREEN}That is alright...{Style.RESET_ALL}"
RETRY_YES_NO = f"{Fore.GREEN}Please type either 'yes' or 'no'.{Style.RESET_ALL}"

BREATHING_INTRO = f"{Fore.GREEN}Would you like to try a breathing exercise...{Style.RESET_ALL}"
QUESTION_BREATHING_1 = f"{Fore.GREEN}Do you wish to start? Type 'yes' or 'skip'.\n{Style.RESET_ALL}"
BREATHING_DETAILS = f"{Fore.GREEN}Let’s do the 4-4-4 exercise...{Style.RESET_ALL}"
QUESTION_BREATHING_START = f"{Fore.GREEN}Shall we start? Type 'start' when ready.\n{Style.RESET_ALL}"
RETRY_YES_SKIP = f"{Fore.GREEN}Please type 'yes' or 'skip'.{Style.RESET_ALL}"
RETRY_START = f"{Fore.GREEN}Please type 'start'.{Style.RESET_ALL}"

AFTER_BREATHING_MSG = f"{Fore.GREEN}Well done!...{Style.RESET_ALL}"
QUESTION_FEELING_AFTER_BREATHING = f"{Fore.GREEN}How are you feeling right now?\n{Style.RESET_ALL}"
REPEAT_BREATHING_PROMPT = f"{Fore.GREEN}If you'd like, we can try it again...{Style.RESET_ALL}"
REPEAT_BREATHING_Q = f"{Fore.GREEN}Would you be interested?\n{Style.RESET_ALL}"
ACK_NO_REPEAT = f"{Fore.GREEN}That's perfectly ok!{Style.RESET_ALL}"

RESPONSES_SENTIMENT = {
    "negative": f"{Fore.GREEN}It's okay to feel this way...{Style.RESET_ALL}",
    "neutral": f"{Fore.GREEN}Got it. Thank you for sharing...{Style.RESET_ALL}",
    "positive": f"{Fore.GREEN}It’s great that you’re feeling good!{Style.RESET_ALL}",
    "default": f"{Fore.GREEN}Hmm, feelings can be confusing...{Style.RESET_ALL}"
}