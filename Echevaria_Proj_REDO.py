# John Leo D. Echevaria (A22-34233) REDO
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
        self.date_pattern = re.compile(r'((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s([0-3]?[0-9]([a-z]{2})?),?\s\d{4})') # Month Day, Year
        self.time_pattern = re.compile(r'\d{1,2}:\d{2}\s?(am|pm)?', re.IGNORECASE) # 12:00 AM
        self.location_pattern = re.compile(r'(?<=Location: ).*') # Location: 912 Example Street
    
    def find(self, pattern):
        """Match the text with the given pattern, returns the match else returns \"None\""""
        match = pattern.search(self.text)
        return match.group() if match else "None"

    def eventName(self):
        self.event_name = self.find(self.event_pattern)
        return self.event_name

    def senderEmail(self):
        self.sender_email = self.find(self.email_pattern)
        return self.sender_email
    
    def senderPhone(self):
        self.sender_phone = self.find(self.phone_pattern)
        return self.sender_phone

    def eventLocation(self):
        self.event_location = self.find(self.location_pattern)
        return self.event_location
    
    def eventDate(self):
        self.event_date = self.find(self.date_pattern)
        return self.event_date
    
    def eventTime(self):
        self.event_time = self.find(self.time_pattern)
        return self.event_time

    def summary(self):
        """Prints the summary of the data gathered from the text files"""
        return f"From: {self.senderEmail()}\n\tEvent: {self.eventName()}\n\tSchedule: {self.eventDate()} {self.eventTime()}\n\tEvent Location: {self.eventLocation()}\n\tSender Phone: {self.senderPhone()}\n\n"

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
