[![EventGenie (Event Planning Assistant)](https://drive.google.com/uc?export=view&id=1fnSFi1U4bZCHAFh3B_QLd5CrjoHzU6Qw "EventGenie")](https://github.com/AkunoCode/EventGenie)

# EventGenie (Event Planner Assistant)
EventGenie is a software that acts as an event planning assistant, helping users to sort and organize events. It extracts information from invitations stored in a specified folder and compiles it into a summary. The software uses regular expressions to identify patterns in the text and returns important details such as the event name, date and time, location, sender's email, and phone number. The summary can be saved as a '.txt' file, '.csv' file or added directly to the Outlook calendar as an appointment using the 'win32com.client' module. With EventGenie, event planning becomes easier and more efficient as it sorts the events from earliest to latest. This makes it easy for users to prioritize and stay on top of their schedule.

This project serves as a prototype for a larger project aimed at accessing and sorting invitation emails directly from a Google account and with its own dedicated GUI.

## Usage
1. Place the text files containing the invitations in the invitation folder or import a folder inside the EventGenie folder and specify the folder name later when prompted by the program.
2. Run the program.
3. The program has navigational text UI that would show you the options for the actions that you can use.

## Properties
* **__text**: A string value that represents the text content of the event invitation.
* **eventName**: A string value that returns the matched event name from the text content.
* **eventDate**: A tuple of datetime objects representing the date and time of the event.
* **eventLocation**: A string value that returns the matched event location from the text content.
* **eventSender**: A tuple of two string values representing the email and phone number of the event sender.
* **dictSummary**: A dictionary value that holds the summary of all properties of the event.

## Methods
* **find(pattern)**: A method that matches the text content with the provided regular expression pattern and returns the matched string.
* **textSummary()**: A method that returns the converted string summary information from the dictSummary().
* **write_txtfile(summary)**: A method that saves the summary as a text file.
* **write_csvfile(summary)**: A method that saves the summary as a comma separated value file.
* **create_schedule(event)**: A method that creates a schedule in Outlook calendar.

## Note
* Please run the program and the folder in the same directory to avoid errors.
* The program only works with text files and only matches specific patterns. Any text that does not match the specified patterns will not be extracted.
* The program is currently set to look for text files in "EventGenie\Invitations" folder by default. You can change the folder when prompted by the program but make sure it is still inside the 'EventGenie' folder. 

## On-Development Planned Features
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1URt9nSAZz3fwQ-8iQ8Od29-37WqGwEH_" alt="EventGenieGUI_Concept">
</p>

* **Graphical User Interface:** To create a GUI for the program to enable visually pleasing and user-friendly access to the program.
* **Added Functions:**
  * **Viewing of full Email Contents**
  * **Editing of Summary Information**
  * **Deletion of Summary Records**
* **Database:** Make use of database to seeminglessly save and view previously accessed datas.
* **Synching with Email Accounts:** Connect with Email accounts such as Google to be able to access data and create summary out of the emails in the user's email inbox.
