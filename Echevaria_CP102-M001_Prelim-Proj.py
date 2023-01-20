# John Leo D. Echevaria (A22-34233)
# CP102 - M001

import os
import re

class Events:
    def __init__(self, text):
        """
        Initialize an object with text, email_pattern,\n 
        phone_pattern, event_pattern, date_pattern properties
        """
        self.text = text
        self.email_pattern = re.compile(r'\w+@\w+\.[a-zA-Z]{2,4}') # echevaria@example.com
        self.phone_pattern = re.compile(r'((\+63)[ -]?(\d{3})[ -]?(\d{3})[ -]?(\d{4}))|(09\d{9})') # +63-929-812-5470 or 09298125470
        self.event_pattern = re.compile(r'\"([A-Z0-9]\w+\s?)+\"') # "Leo's 12th Sample Event"
        self.date_pattern = re.compile(r'((0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.](19|20)?\d{2})|((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s(0?[1-9][a-z]{2}|[12]\d[a-z]{2}|3[01][a-z]{2}),?\s(19|20)?\d{2})') # dd/mm/yyyy or dd-mm-yyyy or Month Day, Year
    
    def find(self, pattern):
        """Match the text with the given pattern, returns the match else returns \"None\""""
        match = pattern.search(self.text)
        return match.group() if match else "None"

    def summary(self):
        """Prints the summary of the data gathered from the text files"""
        # Automatically calls on the find() method with the pattern arguments
        print(f"Event: {self.find(self.event_pattern)}")
        print(f"Schedule: {self.find(self.date_pattern)}")
        print(f"Sender Email: {self.find(self.email_pattern)}")
        print(f"Sender Phone: {self.find(self.phone_pattern)}\n")


print("\nHERE IS THE SUMMARY OF ALL INVITATIONS:\n")

folder_path = "Echevaria_Prelim-Project\Invitations"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"): # text files
        file_path = os.path.join(folder_path, filename) # Combines folder_path with filename to use it as file path for open() function
        with open(file_path, "r") as file: # opens file in read mode only
            text = file.read()
            event_catcher = Events(text) # Creates an event object
            event_catcher.summary() # Prints summary