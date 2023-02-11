from Echevaria_Event import Events
import os
from time import sleep as pause

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