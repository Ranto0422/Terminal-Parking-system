import time
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)

#initiating floor slots availability array

floorSlots = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#plate number slots array
plateNos = [
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
]

#check in time records array
check_in_time = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#floors option array
floorName = ["A. First Floor", "B. Second Floor", "C. Third Floor", "D. Fourth Floor", "E. Fifth Floor"]

#floor parking counter array
flrCounter = [0, 0, 0, 0, 0]

#tickets released
ticketsReleased = 999
ticketCounter = 0

#initiating floor by floor slot counter
flrCounter_memory = 0

#for Car check-in process
def check_in():
    print (f"{floorName[counter]} Parking")
    print("")
    plateNos[counter][flrCounter_memory] = input("Enter the plate number:")
    floorSlots[counter][flrCounter_memory] = 1
    print("")
    print("Processing...")
    print("")
    time.sleep(1)
    hour = current_datetime.hour
    minute = current_datetime.minute
    formatted_time = f"{hour:02d}:{minute:02d}"
    check_in_time[counter][flrCounter_memory] = formatted_time
    print("Checked in successfully")
    print (" Plate number:", plateNos[counter][flrCounter_memory],"\n","Time of Entry:",f"Time:{hour}:{minute}","\n","Ticket No.",ticketCounter)
    start_time = time.time()
    flrCounter[counter] += 1
    time.sleep(1)


#main program
start = "y"
while start == "y":
    print("")
    print("Welcome to Car Parking System Menu")
    print("")
    print(" 1. Car Check-in.\n 2. Car Payment and Exit.\n 3. Floor Maintenance.\n 4. Generate Report.\n 5. Exit Program")
    print("")

    chosenOption = input ("Choose an option. (1/2/3/4/5): ")
    while chosenOption not in ["1", "2", "3", "4", "5"]:
        print("")
        print("Invalid input. Try Again.")
        chosenOption = input ("Choose a valid option. (1/2/3/4/5): ")
    print("")
    time.sleep(0.1)
    
    counter = 0
    if chosenOption == "1":
        print("Available parking slots per floor")
        print("")
        while counter < 5:
            availSlot = 0
            for value in floorSlots[counter]:
                if value == 0:
                    availSlot += 1
            print(floorName[counter], ":", availSlot)
            counter += 1
            
        floorOption = input("Which floor would the customer want to park?(A/B/C/D/E): ").upper()
        print("")
        while floorOption not in ["A", "B", "C", "D", "E"]:
            print("Invalid input. Try Again.")
            floorOption = input("Which floor would the customer want to park?(A/B/C/D/E): ").upper()
            print("")

        ticketCounter += 1
        
        if floorOption == "A":
            counter = 0
            flrCounter_memory = flrCounter[0]
            check_in()
            
        elif floorOption == "B":
            counter = 1
            flrCounter_memory = flrCounter[1]
            check_in()

        elif floorOption == "C":
            counter = 2
            flrCounter_memory = flrCounter[2]
            check_in()

        elif floorOption == "D":
            counter = 3
            flrCounter_memory = flrCounter[3]
            check_in()
            
        else:
            counter = 4
            flrCounter_memory = flrCounter[4]
            check_in()
    
    elif chosenOption == "2":
        print("Check-out in progress")
    elif chosenOption == "3":
        print("Floor maintenance in progress")
    elif chosenOption == "4":
        print("Generate Report")
    elif chosenOption == "5":
        print("Shutting down...")
        time.sleep(2)
        print("")
        print("Program Closed")
        break
