# Event Invitation Summarizer
This program is used to extract information from text files in a given folder. The extracted information includes the event name, schedule, sender's email, and sender's phone number. The program uses regular expressions to match the text with specific patterns.

## Usage
1. Place the text files containing the invitations in a folder.
2. Update the folder_path variable in the program to the path of the folder containing the text files.
Run the program.
3. The program will automatically extract the information and print a summary for each text file in the specified folder.

## Properties
* text: The text to be parsed
* email_pattern: Regular expression pattern for matching email addresses
* phone_pattern: Regular expression pattern for matching phone numbers
* event_pattern: Regular expression pattern for matching event names
* date_pattern: Regular expression pattern for matching dates
## Methods
* find(pattern): Matches the text with the given pattern and returns the match. Returns "None" if no match is found.
* summary(): Prints the summary of the data gathered from the text files.
## Note
* The program only works with text files and only matches specific patterns. Any text that does not match the specified patterns will not be extracted.
* The program is currently set to look for text files in "Echevaria_Prelim-Project\Invitations" folder. Make sure to change the folder path variable to the correct path before running the program.