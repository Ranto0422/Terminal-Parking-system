import time
from datetime import datetime
floor_count = 5
spot_count = 16

check_in_times = {}
parking_fee_per_hour = 40

floor_1 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_2 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_3 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_4 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_5 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
parking_lot = [floor_1,floor_2,floor_3,floor_4,floor_5]
ticket=("F1","F2","F3","F4","F5")

A = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
B = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
C = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
D = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
E = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
parking_lot_num = [A,B,C,D,E]

def change_fee():
    global parking_fee_per_hour
    new_fee = input("Enter the new parking fee per hour: ")
    if new_fee.isnumeric():
        new_fee = float(new_fee)
        if new_fee >= 0:
            parking_fee_per_hour = new_fee
            print("Parking fee updated successfully.")
        else:
            print("Invalid fee. Fee must be a non-negative number.")
    else:
        print("Invalid input. Please enter a valid number for the fee.")
        
def display_parking_lot_num():
    floor_number = 1
    for floor in parking_lot_num:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1
        
def display_parking_lot():
    floor_number = 1
    for floor in parking_lot:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1

def check_in_vehicle():
    global plate_num, ticket_number, check_in_times
    plate_num = input("Enter vehicle plate number: ").strip().upper()
    while not valid_plate(plate_num):
        print("Invalid plate number. Please enter a valid plate number (e.g., ABC 1234).")
        plate_num = input("Enter vehicle plate number: ").strip().upper()
        

    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()

    ticket_number = f"F{floor_choice}-S{spot_choice}"
    
    parking_lot[floor_choice - 1][spot_choice - 1] = "|1|"
    parking_lot_num[floor_choice - 1][spot_choice - 1] = "/"
    check_in_times[ticket_number] = datetime.now()

    print(f"Vehicle with plate number {plate_num} parked on Floor {floor_choice}, Spot {spot_choice}.")
    print(f"Ticket number: {ticket_number}")
    now = datetime.now()
    formated_time = now.strftime("%m-%d %H:%M")
    print("Date and time of check-in (MM/DD H/M):", formated_time )#paltan format
    save_car_information(plate_num, ticket_number, check_in_times, None)
    return

def get_floor_choice():
    display_parking_lot_num()
    while True:
        floor_choice = input("Enter desired floor (1-5): ")
        if floor_choice.isnumeric() and 1 <= int(floor_choice) <= floor_count:
            return int(floor_choice)
        print("Entered floor does not exist.")

def get_spot_choice():
    while True:
        spot_choice = input("Enter desired parking spot (1-16): ")
        if spot_choice.isnumeric() and 1 <= int(spot_choice) <= spot_count:
            return int(spot_choice)
        print("Entered parking spot does not exist.")

def check_out():
    global check_out_time
    while True:
        ticket_number = input("Enter the ticket number for check-out: ").strip().upper()
        check_in_time = check_in_times.get(ticket_number)

        if not check_in_time:
            print(f"Invalid ticket number: {ticket_number}")
        else:
            break
     # Calculate the parking fee
    check_out_time = datetime.now()
    parked_duration = check_out_time - check_in_time
    hours_parked = (parked_duration.total_seconds() + 3600 - 1) // 3600
    hours_parked_actual= parked_duration.total_seconds() / 3600
    total_fee = parking_fee_per_hour * hours_parked
    print(f"Vehicle with ticket number {ticket_number} has been parked for {hours_parked_actual:.2f} hours.")
    print(f"Total parking fee: ₱{total_fee:.2f}")

    # Save car information with check-out time
    save_car_information(plate_num, ticket_number, check_in_time, check_out_time)

     # Clear the parking spot
    floor, spot = extract_floor_and_spot(ticket_number)
    clear_parking_spot(floor, spot)

    # Remove the check-in record
    remove_check_in_record(ticket_number)

def extract_floor_and_spot(ticket_number):
    # Extract the floor and spot numbers from the ticket
    floor_str, spot_str = ticket_number[1:].split("-S")
    floor = int(floor_str)
    spot = int(spot_str)
    return floor, spot
def clear_parking_spot(floor, spot):
    # Mark the parking spot as available
    parking_lot[floor - 1][spot - 1] = '0'
    parking_lot_num[floor - 1][spot - 1] = '1'
def remove_check_in_record(ticket_number):
    # Remove the check-in record
    if ticket_number in check_in_times:
        del check_in_times[ticket_number]

def disable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['UM'] * spot_count
    print(f"Floor {floor_choice} has been disabled.")

def enable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['0'] * spot_count
    print(f"Floor {floor_choice} has been enabled.")

def disable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = 'UM'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been disabled.")

def enable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = '0'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been enabled.")

def save_car_information(plate_num, ticket_number, check_in_time, check_out_time):
    filename = "car_information.txt"
    with open(filename, "a") as file:
        file.write(f"Plate Number: {plate_num}\n")
        file.write(f"Ticket Number: {ticket_number}\n")
        file.write(f"Check-In Time: {check_in_time}\n")
        file.write(f"Check-Out Time: {check_out_time}\n")
        file.write("\n")

def valid_plate(plate_num):
    plate_num = plate_num.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    if len(plate_num) == 7 and plate_num[:3].isalpha() and plate_num[3:].isdigit():
        return True
    return False
#def save
def design(): 
   print("  ______                     ______                   ______ ")#sana bet nio
   print(" /|_||_\\`.__                /|_||_\\`.__              /|_||_\\`.__")
   print("(   _    _ _\\    ......    (   _    _ _\\    .....   (   _    _ _\\ ")
   print("=`-(_)--(_)-'              =`-(_)--(_)-'            =`-(_)--(_)-'")
   print("                                                  ")
   print("           WELCOME TO PARKING MANAGEMENT AND BILLING SYSTEM")
   print("                          by Ilao Corporation.           ")
   print("                ______                    ______")
   print("               /|_||_\`.__               /|_||_\`.__")
   print("              (   _    _ _\\   ......    (   _    _ _\\")
   print("             =`-(_)--(_)-'             =`-(_)--(_)-' ")
   print('   ')
   print("                      Press enter to continue.. ")
   try:
       input()
   except print(''):
        pass

def main():
    global plate_num, ticket_number, check_in_times, check_out_time
    while True:
        print("How can we help you today?")
        print("----- Parking Services -----") #medj pinalitan
        print("1. Display available floors")
        print("2. Check-in a vehicle")
        print("3. Check-out and payment")
        print("---- Maintenance -----")
        print("4. Disable a floor/parking spot")
        print("5. Enable a floor/parking spot")
        print("----- Others -----") 
        print("6. Display and save current reports")
        print("7. Change parking fee")
        print("8. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_parking_lot()
            input ("Please press enter to go to menu")
            
        elif choice == "2":
            check_in_vehicle()
            display_parking_lot()
        elif choice == "3":
            check_out() # Add code for check-out and payment
        elif choice == "4":
            disable_choice = input("a. Disable parking floor\nb. Disable parking spot\nEnter your choice: ") .lower()
            while disable_choice not in ["a","b"]:
                disable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if disable_choice == "a":
                disable_floor()
            elif disable_choice == "b":
                disable_spot()
        elif choice == "5":
            enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice: ").lower()
            while enable_choice not in ["a","b"]:
                enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if enable_choice == "a":
                enable_floor()
            elif enable_choice == "b":
                enable_spot()
        elif choice == "6":
            save_car_information(plate_num, ticket_number, check_in_times, check_out_time)  # Add code for displaying and saving reports
        elif choice == "7":
            change_fee()  # Add code for changing parking fee
        elif choice == "8":
            print("The program is exiting.")
            time.sleep(1)
            print("Have a nice Day!")
            try_again = input("Thank you! Would you like to blablabla: ").lower().upper()
            if try_again == "yes":
                break
            if try_again == "no":
                print("Thank you, come again!")
                break

        else:
            print("Invalid choice. Please enter a valid option (1-8).")
design()
main()
