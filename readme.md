# Event Invitation Summarizer
This program is used to extract information from invitations (text files) in a given folder. The extracted information includes the event name, schedule (date and time), location, sender's email, and sender's phone number. The program uses regular expressions to match the text with specific patterns and returns it to either print or write on another text file.

This project is created as a mock-up for a bigger project that aims to directly access emails from your google account to fetch and sort the invitations in your email.

## Usage
1. Place the text files containing the invitations in the invitation folder.
2. Run the program.
3. The program will automatically extract the information and print a summary for each text file in the specified folder.
4. The program will then prompt you if you want to create a text file containing the summary of the events from the invitations.

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
* write_file(summary): A method that prompts the user to save the summary as a text file.
## Note
* The program only works with text files and only matches specific patterns. Any text that does not match the specified patterns will not be extracted.
* The program is currently set to look for text files in "Echevaria_Prelim-Project\Invitations" folder. If you wish to use a different folder for invitations please make sure to change the folder path variable to the correct path before running the program.