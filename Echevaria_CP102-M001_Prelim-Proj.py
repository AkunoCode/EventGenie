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
        return f"Event: {self.find(self.event_pattern)}\nSchedule: {self.find(self.date_pattern)}\nSender Email: {self.find(self.email_pattern)}\nSender Phone: {self.find(self.phone_pattern)}\n\n"

    def write_file(self, summary):
        """Prompts the user if they want to save the summary on a txt file"""
        while True:
            save = input("Save summary to file? (yes/no): ").lower()
            if save in ["yes","no"]:
                if save == "yes":
                    with open("Invitations_Summary.txt","w") as file:
                        file.write(summary)
                    print("File saved as 'Invitations_Summary.txt'")
                break
            else:
                print("Please answer 'yes' or 'no'")

def main():
    folder_path = "Invitations"
    summary = ""

    print("\nHERE IS THE SUMMARY OF ALL INVITATIONS:\n")

    for filename in os.listdir(folder_path): # os directory
        if filename.endswith(".txt"): # text files
            file_path = os.path.join(folder_path, filename) # Combines folder_path with filename to use it as file path for open() function
            with open(file_path, "r") as file: # opens file in read mode only
                text = file.read()
                event_catcher = Events(text) # Creates an event object
                summary += event_catcher.summary()

    print(summary) # Prints summary
    event_catcher.write_file(summary)

if __name__ == "__main__":
    main()
