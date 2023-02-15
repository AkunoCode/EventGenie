import sys
from Echevaria_Event import Events
import os
from time import sleep as pause

def intro():
    folder_path = ""
    if os.path.exists(os.path.abspath('Invitations_Summary.txt')):
        if input("'Invitations_Summary.txt' already exists. Would you like to read it? [Y/N]: ").lower() == "y":
            with open('Invitations_Summary.txt',"r") as file:
                for i in file.readlines():
                    print(i,end="")
                    pause(0.1)

    print("\nThis program is set to read on the text files located in the 'Invitations' folder\n")
    print("Choose an operation to perform:")
    print("[1] Create New Summary")
    print("[2] Change Folder Name")
    print("[3] Exit")

    choice = 0
    while True:
        choice = input()
        if choice == "1":
            start()
            break

        elif choice == "2":
            folder_path = folderChange()
            print(f"Folder name changed to '{folder_path}'\n")
            print("Choose an operation to perform:")
            print("[1] Create New Summary (this will overwrite the existing one)")
            print("[2] Exit")
            while True:
                choice = input()
                if choice == "1":
                    start(folder_path)
                    break
                elif choice == "2":
                    exit()
                else:
                    print("Please choose among the available options.")

        elif choice == "3":
            exit()
        else:
            print("Please choose among the available options.")

def folderChange():
    while True:
        folder_path = input("\nPlease type the new folder name to search for: ").lower()
        if os.path.exists(os.path.abspath(folder_path)):
            break
        else:
            print("\nNo such folder found in the directory.\nPlease make sure you are providing the correct folder name and place the folder in the same directory as the code to avoid errors.\n")
    return folder_path

def exit():
    print("\nThank you!\nJohn Leo D. Echevaria (A22-34233)")
    pause(5)
    sys.exit()

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
                    event_list.append(event.dictSummary) # Adds the summary of the event object to the list
    
    except FileNotFoundError:
        print("Folder not found in the directory.\nPlease make sure that the folder containing the text files is located inside the same directory as the program.\nThen run the program inside the directory")
    
    event_list.sort(key= lambda x: x["Event Date"]) # Sorts the list by value of "Event Date" (Earliest to Latest)

    events_text = [] 
    for i in event_list:
        event_str = event.textSummary(i)
        print(event_str)
        events_text.append(event_str)
        pause(1)
    
    
    print("\nChoose an operation to perform:")
    print("[1] Save as a '.txt' file.")
    print("[2] Save as a 'csv' file.")
    print("[3] Create Schedule in Outlook Calendar.")
    print("[4] Exit")

    while True:
        choice = input()
        if choice == "1":
            event.write_txtfile("".join(events_text))
            print("File saved as 'Invitations_Summary.txt'")
            break
        elif choice == "2":
            for i in event_list:
                i.pop("Event Body")
                event.write_csvfile(i)
            print("File saved as 'Invitations_Summary.txt'")
            break    
        elif choice == "3":
            for i in event_list:
                event.create_schedule(i)
            print("Events saved in your Outlook calendar.")
            break
        elif choice == "4":
            exit()
        else:
            print("Please choose among the available options.")
    pause(3)

    print("\nThank you!\nJohn Leo D. Echevaria (A22-34233)")
    pause(5)

if __name__ == "__main__":
    intro()