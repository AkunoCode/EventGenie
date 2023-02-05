# John Leo D. Echevaria (A22-34233)
# CP102 - M001

import os
import re
import datetime
import win32com.client
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

    @property
    def summary(self):
        """Returns a Summary Dictionary of the properties of the Event Object"""
        event_dict = {
            "Event Name": self.eventName,
            "Event Date": self.eventDate[0],
            "Event Time": self.eventDate[1],
            "Event Location": self.eventLocation,
            "Sender Email": self.eventSender[0],
            "Sender Phone": self.eventSender[1],
            "Event Body" : self.text
        }
        return event_dict
    
    def find(self, pattern):
        """Match the text with the given pattern, returns the match else returns "Not Found\""""
        match = pattern.search(self.text)
        return match.group() if match else "Not Found"

    def write_file(self, summary):
        """Save the string summary of the invitations in a txt file"""
        with open("Invitations_Summary.txt","w") as file:
            file.write(summary)
        print("File saved as 'Invitations_Summary.txt'")

    def create_schedule(self, event):
        """Creates a schedule in outlook using the win32com.client"""
        outlook = win32com.client.Dispatch("Outlook.Application") # Creates an instance of Microsoft outlook
        appointment = outlook.CreateItem(1) # argument "1" means we are creating an appointment
        appointment.Subject = event["Event Name"]
        appointment.Start = event["Event Date"].strftime("%Y-%m-%d")
        appointment.Location = event["Event Location"]
        appointment.Body = event["Event Body"]
        appointment.ReminderSet = True
        appointment.ReminderMinutesBeforeStart = 15
        appointment.Save()

def main():
    while True:
        folder_path = input("\nThis program is set to read on the text files located in the Invitation folder.\n\nWould you like to update the folder name?\nIf yes, please type the folder name containing text files or type \"no\": ").lower()
        if folder_path == "no":
            start() # Calls the start function with default arguments
            break
        elif os.path.exists(os.path.abspath(folder_path)):
            start(folder_path) # Calls the start function with the folder_path as an argument
            break
        else:
            print("\nNo such folder found in the directory.\nPlease make sure you are providing the correct folder name and place the folder in the same directory as the code to avoid errors.")

def start(folder_path="Invitations"):
    abs_folder_path = os.path.abspath(folder_path) # Creates absolute path from the provided relative path
    event_list = []

    print("\nDISCLAIMER:\nThe program uses specific patterns to match information inside the invitation.\nDue to this feature, other formats of the information may not get matched and return Not Found.\nIt may also return Not Found if no such information is present in the invitation...\n") 
    print("Extracting information from the text files...\n")
    pause(10)
    print(f"Summary of events from the {abs_folder_path}:\n")
    pause(1)

    try:
        for filename in os.listdir(folder_path): # os directory
            if filename.endswith(".txt"): # text files
                file_path = os.path.join(abs_folder_path, filename) # Combines folder_path with filename to use it as file path for open() function
                with open(file_path, "r") as file: # opens file in read mode only
                    text = file.read()
                    event = Events(text) # Creates an event object
                    event_list.append(event.summary) # Adds the summary of the event object to the list
    
    except FileNotFoundError:
        print("Folder not found in the directory.\nPlease make sure that the folder containing the text files is located inside the same directory as the program.\nThen run the program inside the directory")
    
    event_list.sort(key= lambda x: x["Event Date"]) # Sorts the list by value of "Event Date" (Earliest to Latest)
        
    event_str = ""
    for i in event_list:
        for k,v in i.items():
            if k == "Event Body":
                continue
            else:
                event_str += f"{k}: {v}\n"
        event_str += "\n"
    print(event_str)
    pause(1)
    
    while True:
        save_write = input("Would you like to schedule the events in your calendar or just save it as a text file? (\"schedule\"/\"save\"): ")
        if save_write == "save":
            event.write_file(event_str)
            break
        elif save_write == "schedule":
            for i in event_list:
                event.create_schedule(i)
            print("Events saved in your Outlook calendar.")
            break
        else:
            print("Please type either \"schedule\" or \"save\".")
    pause(3)

    print("\nThank you!\nJohn Leo D. Echevaria (A22-34233)")
    pause(5)

if __name__ == "__main__":
    main()