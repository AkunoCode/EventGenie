# EventGenie (Event Planner Assistant)
EventGenie is a software that acts as an event planning assistant, helping users to sort and organize events. It extracts information from invitations stored in a specified folder and compiles it into a summary. The software uses regular expressions to identify patterns in the text and returns important details such as the event name, date and time, location, sender's email, and phone number. The summary can be saved as a text file or added to the Outlook calendar using the 'win32com.client' module. With EventGenie, event planning becomes easier and more efficient as it sorts the events from earliest to latest. This makes it easy for users to prioritize and stay on top of their schedule.

This project serves as a prototype for a larger project aimed at accessing and sorting invitation emails directly from a Google account.

## Usage
1. Place the text files containing the invitations in the invitation folder or import a folder inside the Echevaria_Prelim-Proj folder and specify the folder name later when prompted by the program.
2. Run the program.
3. The program will automatically extract the information and print a summary for each text file in the specified folder.
4. The program will then prompt you if you want to create a text file containing the summary of the events from the invitations or schedule the events in your Outlook calendar.

## Properties
* text: A string value that represents the text content of the event invitation.
* eventName: A string value that returns the matched event name from the text content.
* eventDate: A tuple of datetime objects representing the date and time of the event.
* eventLocation: A string value that returns the matched event location from the text content.
* eventSender: A tuple of two string values representing the email and phone number of the event sender.
* event_dict: A dictionary value that holds the summary of all properties of the event.
## Methods
* find(pattern): A method that matches the text content with the provided regular expression pattern and returns the matched string.
* summary(): A method that returns the summary of all properties of the event as a dictionary.
* write_file(summary): A method that saves the summary as a text file.
* create_schedule(event): A method that creates a schedule in Outlook calendar
## Note
* Please run the program and the folder in the same directory to avoid errors.
* The program only works with text files and only matches specific patterns. Any text that does not match the specified patterns will not be extracted.
* The program is currently set to look for text files in "Echevaria_Prelim-Project\Invitations" folder by default. You can change the folder when prompted by the program but make sure it is still inside the 'Echevaria_Pelim-Project' folder. 