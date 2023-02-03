# John Leo D. Echevaria (A22-34233)
# CP102 - M001

import os
import re
import datetime
from time import sleep as pause

class Events:
    def __init__(self, text):
        """
        Initialize an Event object
        """
        self.text = text
    
    @property 
    def eventName(self):
        """Returns the Matched Event Name"""
        event_pattern = re.compile(r'\"([A-Z0-9]\w+\s?)+\"') # "Leo's 12th Sample Event"
        return self.find(event_pattern)
    
    @property 
    def eventDate(self):
        """Returns a tuple of Date and Time Object"""
        date_pattern = re.compile(r'((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s([0-3]?[0-9](?=([a-z]{2})?)),?\s\d{4})') # Month Day, Year
        time_pattern = re.compile(r'\d{1,2}:\d{2}\s?(am|pm)?', re.IGNORECASE) # 12:00 AM
        date = self.find(date_pattern)
        time = self.find(time_pattern)

        # Convert the date and time into a datetime object
        if time != "Not Found":
            time = datetime.datetime.strptime(time, '%I:%M %p').time()
        if "," in date:
            date = datetime.datetime.strptime(date, '%B %d, %Y').date()
        else:
            date = datetime.datetime.strptime(date, '%B %d %Y').date()
        return (date,time)
    
    @property 
    def eventLocation(self):
        """Returns the Matched Event Location"""
        location_pattern = re.compile(r'(?<=Location: ).*') # Location: 912 Example Street
        return self.find(location_pattern)

    @property 
    def eventSender(self):
        """Returns the Matched Event Sender's Email and Phone Number"""
        email_pattern = re.compile(r'[\w.]+@\w+\.[a-zA-Z]{2,4}') # echevaria@example.com
        phone_pattern = re.compile(r'((\+63)[ -]?(\d{3})[ -]?(\d{3})[ -]?(\d{4}))|(09\d{9})') # +63-929-812-5470 or 09298125470
        return (self.find(email_pattern),self.find(phone_pattern))
    
    def find(self, pattern):
        """Match the text with the given pattern, returns the match else returns "Not Found\""""
        match = pattern.search(self.text)
        return match.group() if match else "Not Found"

    def summary(self):
        """Returns a Summary Dictionary of the properties of the Event Object"""
        event_dict = {
            "Event Name": self.eventName,
            "Event Date": self.eventDate[0],
            "Event Time": self.eventDate[1],
            "Event Location": self.eventLocation,
            "Sender Email": self.eventSender[0],
            "Sender Phone": self.eventSender[1]
        }
        return event_dict

    def write_file(self, summary):
        """Prompts the user if they want to save the summary on a txt file"""
        while True:
            save = input("Save summary to a text file? (yes/no): ").lower()
            if save in ["yes","no"]:
                if save == "yes":
                    with open("Invitations_Summary.txt","w") as file:
                        file.write(summary)
                    print("File saved as 'Invitations_Summary.txt'")
                break
            else:
                print("Please answer 'yes' or 'no'")


def main():
    folder_path = input("\nThis program is set to read on the text files located at the Invitation folder.\nWould you like to update the folder path?\nIf yes, please type the path to the folder containing text files. If no, please type \"no\": ").lower()
    if folder_path == "no":
        start()
    elif os.path.exists(folder_path):
        start(folder_path)
    else:
        print("\nNo such folder found in the directory. Please make sure you are providing a correct path to the folder to avoid errors.")
        main()


def start(path="Invitations"):
    folder_path = path
    event_list = []

    print("\nDISCLAIMER:\nThe program uses specific patterns to match information inside the invitation.\nDue to this feature, other formats of the information may not get matched and return Not Found.\nIt may also return Not Found if no such information is present in the invitation...\n") 
    pause(10)
    print("Extracting information from the text files...\n")
    pause(3)
    print(f"Summary of events from the {path}:\n")
    pause(1)

    for filename in os.listdir(folder_path): # os directory
        if filename.endswith(".txt"): # text files
            file_path = os.path.join(folder_path, filename) # Combines folder_path with filename to use it as file path for open() function
            with open(file_path, "r") as file: # opens file in read mode only
                text = file.read()
                event = Events(text) # Creates an event object
                event_list.append(event.summary()) # Adds the summary of the event object to the list
    
    event_list.sort(key= lambda x: x["Event Date"]) # Sorts the list by value of "Event Date" (Earliest to Latest)
    
    event_str = ""
    for i in event_list:
        for k,v in i.items():
            event_str += f"{k}: {v}\n"
        event_str += "\n"
    print(event_str)
    pause(1)
    
    event.write_file(event_str)
    pause(3)
    
    print("\nThank you!\n-John Leo D. Echevaria (A22-34233)")
    pause(5)

if __name__ == "__main__":
    main()