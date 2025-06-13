import time
import re

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