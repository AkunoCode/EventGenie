# John Leo D. Echevaria (A22-34233)
# CP102 - M001

import re
import csv
import datetime
import win32com.client

class Events:
    def __init__(self, text):
        """
        Initialize an Event object
        """
        self.__text = text
    
    @property 
    def eventName(self):
        """Returns the Matched Event Name"""
        event_pattern = re.compile(r'\"(\w+\s?)+\"') # "Leo's 12th Sample Event"
        return self.find(event_pattern)
    
    @property 
    def eventDate(self):
        """Returns a tuple of Date and Time Object"""
        date_pattern = re.compile(r'((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s([0-3]?[0-9](?=([a-z]{2})?)),?\s\d{4})') # Month Day, Year
        time_pattern = re.compile(r'\d{1,2}:\d{2}\s?(am|pm)?', re.IGNORECASE) # 12:00 AM
        date = self.find(date_pattern)
        time = self.find(time_pattern)

        # Convert time into a datetime object
        if time == "Not Found":
            time = datetime.time(0, 0)
        elif ":" in time:
            time = datetime.datetime.strptime(time, '%I:%M %p').time()
        else:
            time = datetime.time(0, 0)

        # Convert date into datetime object
        if date == "Not Found":
            date = datetime.date.today()
        elif "," in date: # To avoid errors in cases where the date is formatted with a "," after the day.
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
    def dictSummary(self):
        """Returns a Summary Dictionary of the properties of the Event Object"""
        event_dict = {
            "Event Name": self.eventName,
            "Event Date": self.eventDate[0],
            "Event Time": self.eventDate[1],
            "Event Location": self.eventLocation,
            "Sender Email": self.eventSender[0],
            "Sender Phone": self.eventSender[1],
            "Event Body" : self.__text
        }
        return event_dict
    
    def find(self, pattern):
        """Match the text with the given pattern, returns the match else returns "Not Found\""""
        match = pattern.search(self.__text)
        return match.group() if match else "Not Found"

    def write_txtfile(self, summary):
        """Save the string summary of the invitations in a txt file"""
        with open("Invitations_Summary.txt","w") as file:
            file.write(summary)
    
    def write_csvfile(self, dictSummary):
        with open("Invitations_Summary.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=dictSummary.keys())
            writer.writeheader()
            writer.writerow(dictSummary)
    
    def textSummary(self, dictSummary):
        event_str = ""
        for k,v in dictSummary.items():
            if k == "Event Body":
                continue
            else:
                event_str += f"{k}: {v}\n"
        event_str += "\n"
        
        return event_str

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