import time
import re
from colorama import Fore, Style

class TextPauses:
    def __init__(self, text):
        self.text = text

    def display(self):
        # Match [[pause=2]], [[pause=1.5]], etc.
        parts = re.split(r"(\[\[pause=[0-9.]+\]\])", self.text)

        for part in parts:
            match = re.match(r"\[\[pause=([0-9.]+)\]\]", part)
            if match:
                pause_time = float(match.group(1))
                time.sleep(pause_time)
            else:
                print(part, end='', flush=True)
        print()  # final line break
