import sys
from Echevaria_Event import Events
import os
import csv
from time import sleep as pause

os.system('cls')

def read():
    if os.path.exists(os.path.abspath('Invitations_Summary.txt')):
        if input("'Invitations_Summary.txt' already exists. Would you like to read it? [Y/N]: ").lower() == "y":
            os.system('cls')
            with open('Invitations_Summary.txt',"r") as file:
                for i in file.readlines():
                    print(i,end="")
                    pause(0.1)

    elif os.path.exists(os.path.abspath('Invitations_Summary.csv')):
        if input("'Invitations_Summary.csv' already exists. Would you like to read it? [Y/N]: ").lower() == "y":
            os.system('cls')
            with open('Invitations_Summary.csv',"r") as file:
                reader = csv.reader(file)
                next(reader) # Skip the header row
                for row in reader:
                    print(f"Event Name: {row[0]}")
                    print(f"Event Date: {row[1]}")
                    pause(0.1)
                    print(f"Event Time: {row[2]}")
                    pause(0.1)
                    print(f"Event Location: {row[3]}")
                    pause(0.1)
                    print(f"Event Sender Email: {row[4]}")
                    pause(0.1)
                    print(f"Event Sender Phone: {row[5]}")
                    pause(0.1)
                    print("")        
    else:
        print("\nNo existing summary file found.")
        pause(1)

def folderChange():
    while True:
        folder_path = input("\nPlease type the new folder name to search for: ")
        if os.path.exists(os.path.abspath(folder_path)):
            break
        else:
            print("\nNo such folder found in the directory.\nPlease make sure you are providing the correct folder name and place the folder in the same directory as the code to avoid errors.\n")
    return folder_path

def exit():
    print("\nThank you!\nJohn Leo D. Echevaria (A22-34233)")
    pause(5)
    sys.exit()

def main():
    folder_path = ""

    print("\nThis program is set to read on the text files located in the 'Invitations' folder\n")
    print("Choose an operation to perform:")
    print("[1] Create New Summary")
    print("[2] Change Folder Name")
    print("[3] Exit")

    choice = 0
    while True:
        choice = input()
        if choice == "1":
            os.system('cls')
            start_extract()
            break

        elif choice == "2":
            os.system('cls')
            folder_path = folderChange()
            print(f"Folder name changed to '{folder_path}'\n")
            print("Choose an operation to perform:")
            print("[1] Create New Summary")
            print("[2] Exit")
            while True:
                choice = input()
                if choice == "1":
                    os.system('cls')
                    start_extract(folder_path)
                    break
                elif choice == "2":
                    os.system('cls')
                    exit()
                else:
                    print("Please choose among the available options.")

        elif choice == "3":
            os.system('cls')
            exit()
        else:
            print("Please choose among the available options.")



def start_extract(folder_path="Invitations"):
    abs_folder_path = os.path.abspath(folder_path) # Creates absolute path from the provided relative path
    event_list = []

    print("\nDISCLAIMER:\nThe program uses specific patterns to match information inside the invitation.\nDue to this feature, other formats of the information may not get matched and return Not Found.\nIt may also return Not Found if no such information is present in the invitation...\n") 
    pause(1)
    print("Extracting information from the text files...")
    pause(10)

    try:
        for filename in os.listdir(folder_path): # os directory
            if filename.endswith(".txt"): # text files
                file_path = os.path.join(abs_folder_path, filename) # Combines folder_path with filename to use it as file path for open() function
                with open(file_path, "r") as file: # opens file in read mode only
                    text = file.read()
                    event = Events(text) # Creates an event object
                    event_list.append(event) # Adds the summary of the event object to the list
    
    except FileNotFoundError:
        print("Folder not found in the directory.\nPlease make sure that the folder containing the text files is located inside the same directory as the program.\nThen run the program inside the directory")
    
    print("\nEvent Data Extracted.")  
    pause(1)

    while True:
        os.system('cls')
        if input("\nWould you like to sort the events by order of most recent to latest? [Y/N]: ").lower() == "y":
            event_list.sort(key= lambda x: x.dictSummary["Event Date"]) # Sorts the list by value of "Event Date" (Earliest to Latest)
            print("\nEvents Sorted.")
            break
        else:
            break  
    
    pause(2)
    os.system('cls')
    print("\nChoose an operation to perform:")
    print("[1] Print Summary")
    print("[2] Save as a '.txt' file.")
    print("[3] Save as a '.csv' file.")
    print("[4] Create Schedule in Outlook Calendar.")
    print("[5] Exit")

    while True:
        choice = input()
        if choice == "1":
            os.system('cls')
            print(f"\nSummary of events from the {abs_folder_path}:\n")
            for i in event_list:
                event_str = i.textSummary()
                print(event_str)
                pause(1)
            exit()
        elif choice == "2":
            os.system('cls')
            event.write_txtfile(event_list)
            print("File saved as 'Invitations_Summary.txt'. You can read the file after restarting the program")
            break
        elif choice == "3":
            os.system('cls')
            csv_list = [["Event Name","Event Date","Event Time","Event Location","Sender Email","Sender Phone"],]
            for i in event_list:
                i = i.dictSummary
                i.pop("Event Body")
                csv_list.append(i.values())
            event.write_csvfile(csv_list)
            print("File saved as 'Invitations_Summary.csv'. You can read the file after restarting the program")
            break    
        elif choice == "4":
            os.system('cls')
            for i in event_list:
                i.create_schedule()
            print("Events saved in your Outlook calendar.")
            break
        elif choice == "5":
            exit()
        else:
            print("Please choose among the available options.")

if __name__ == "__main__":
    if os.path.exists(os.path.abspath('Invitations_Summary.csv')) or os.path.exists(os.path.abspath('Invitations_Summary.txt')):
        read()
        main()
    else:
        main()