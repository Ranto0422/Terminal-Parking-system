import time
import os
from datetime import datetime
floor_count = 5
spot_count = 16
released_ticket_counter = 0

check_in_times = {}
parking_fee_per_hour = 40

total_sale=0

max_parking_time = 0
min_parking_time = float('inf')
total_parking_time = 0

floor_1 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_2 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_3 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_4 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_5 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_1 = ["0"] * 16
floor_2 = ["0"] * 16
floor_3 = ["0"] * 16
floor_4 = ["0"] * 16
floor_5 = ["0"] * 16
parking_lot = [floor_1,floor_2,floor_3,floor_4,floor_5]
ticket=("F1","F2","F3","F4","F5")

A = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
B = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
C = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
D = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
E = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
parking_lot_num = [A,B,C,D,E]

fL1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL4 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL5 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
parking_lot_num2 = [fL1,fL2,fL3,fL4,fL5]

Tavailable = 0
def clear_screen():
    os.system('cls')
def availableparking_floor1():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_1[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}: Available Parking space in 1st floor")
    Tavailable = Favailable + Tavailable
def availableparking_floor2():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_2[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 2nd floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor3():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_3[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 3rd floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor4():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_4[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 4th floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor5():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_5[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 5th floor")
    Tavailable=Favailable+Tavailable
    print(f"total available slot:{Tavailable}")
def change_fee():
    global parking_fee_per_hour
    
    while True:
        new_fee = input("Enter the new parking fee per hour (input 'Q' to quit): ").strip().upper()
        
        if new_fee == 'Q':
            print("Exiting fee change process.")
            break
        
        if new_fee.isnumeric():
            new_fee = float(new_fee)
            if new_fee >= 0:
                parking_fee_per_hour = new_fee
                print("Parking fee updated successfully.")
                input("Enter To Continue")
                break  # Exit the loop after updating the fee
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
    global plate_num, ticket_number, check_in_times, total_fee
    global released_ticket_counter

    while True:
        plate_num = input("Enter vehicle plate number (input 'Q' to quit): ").strip().upper()
        if plate_num == "Q":
            print("Exiting check-in process.")
            time.sleep(1)
            return
        if is_plate_number_present_in_file(plate_num):
            print("Please enter a different plate number.")
            time.sleep(1)
        elif not (plate_num):
            print("Invalid plate number. Please enter a valid plate number (e.g., ABC 1234).")
        else:
            break

    while True:
        floor_choice = get_floor_choice()
        spot_choice = get_spot_choice()

        if parking_lot[floor_choice - 1][spot_choice - 1] == "|1|" or parking_lot_num[floor_choice - 1][spot_choice - 1] == "UM" or parking_lot_num[floor_choice - 1][spot_choice - 1] == "/":
            print("Spot is occupied. CHOOSE ANOTHER.")
        else:
            break

    ticket_number = f"F{floor_choice}-S{spot_choice}"

    parking_lot[floor_choice - 1][spot_choice - 1] = "|1|"
    parking_lot_num[floor_choice - 1][spot_choice - 1] = "/"
    check_in_times[ticket_number] = datetime.now()

    print(f"Vehicle with plate number {plate_num} parked on Floor {floor_choice}, Spot {spot_choice}.")
    print(f"Ticket number: {ticket_number}")
    now = datetime.now()
    formated_time = now.strftime("%m-%d %H:%M")
    print("Date and time of check-in M/D H/M", formated_time)  # paltan format
    released_ticket_counter = released_ticket_counter + 1
    print("Total Released_ticket: ", released_ticket_counter)
    display_parking_lot()
    save_car_information(plate_num, ticket_number, check_in_times, None, None)
    print("Parking car...")
    time.sleep(1)
    print("PARKED")
    time.sleep(1)
    return
def is_plate_number_present_in_file(plate_num):
    # Check if the plate number is present in the saved car information file
    filename = "car_information.txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("Plate Number:") and plate_num in line:
                    print(f"Plate number {plate_num} is already in the Car Park.")
                    time.sleep(1)
                    return True
    except FileNotFoundError:
        return False
    
    return False
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
    global check_out_time, total_fee, total_sale
    while True:
        ticket_number = input("Enter the ticket number for check-out (input 'Q' to quit): ").strip().upper()
        if ticket_number == "Q":
            print("Exiting Check-in process")
            break
        check_in_time = check_in_times.get(ticket_number)
        if not check_in_time:
            print(f"Invalid ticket number: {ticket_number}")
        else:
            # Calculate the parking fee
            check_out_time = datetime.now()
            parked_duration = check_out_time - check_in_time
            hours_parked = (parked_duration.total_seconds() + 3600 - 1) // 3600
            hours_parked_actual= parked_duration.total_seconds() / 3600
            total_fee = parking_fee_per_hour * hours_parked
            total_sale = total_sale+total_fee
            print(f"Vehicle with ticket number {ticket_number} has been parked for {hours_parked_actual:.2f} hours.")
            print(f"Total parking fee: ₱{total_fee:.2f}")
            while True:
                payment_str = input("Enter Amount paid: ")
                if not payment_str.isnumeric() or float(payment_str) < 0:
                    print("Invalid input. Please enter a valid positive numeric value.")
                    continue

                payment = float(payment_str)

                if payment < total_fee:
                    print("Not enough Payment")
                else:
                    break

            # Calculate change
            change = payment - total_fee
            print("CHANGE", "₱", change)
            input("Enter To Exit")

            # Calculate maximum and minimum parking times
            global max_parking_time, min_parking_time, total_parking_time
            if hours_parked_actual > max_parking_time:
                max_parking_time = hours_parked_actual
            if hours_parked_actual < min_parking_time:
                min_parking_time = hours_parked_actual
            total_parking_time += hours_parked_actual

            # Save car information with check-out time
           # save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee)
            # Clear the parking spot
            floor, spot = extract_floor_and_spot(ticket_number)
            clear_parking_spot(floor, spot)

            # Remove the check-in record
            remove_check_in_record(ticket_number)

            # Get plate number for reporting
            plate_num = get_plate_number_from_file(ticket_number)

            # Call report_logs with the necessary arguments
            report_logs(released_ticket_counter, max_parking_time)

            print("Saving")
            time.sleep(1)
            break
def get_plate_number_from_file(ticket_number):
    filename = "car_information.txt"
    with open(filename, "r") as file:
        for line in file:
            if line.startswith("Ticket Number:") and ticket_number in line:
                # Assuming the plate number is on the line after "Ticket Number:"
                return next(file).strip().split(":")[1].strip()
    return None
def remove_plate_number(plate_num):
    filename = "car_information.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if not (line.startswith("Plate Number:") and plate_num in line):
                    file.write(line)
    except FileNotFoundError:
        pass  
def extract_floor_and_spot(ticket_number):
    # Extract the floor and spot numbers from the ticket
    floor_str, spot_str = ticket_number[1:].split("-S")
    floor = int(floor_str)
    spot = int(spot_str)
    return floor, spot
def clear_parking_spot(floor, spot):
    # Mark the parking spot as available
    parking_lot[floor - 1][spot - 1] = '0'
    parking_lot_num[floor - 1][spot - 1] = parking_lot_num2[floor - 1][spot - 1]
def remove_check_in_record(ticket_number):
    # Remove the check-in record from the dictionary
    if ticket_number in check_in_times:
        del check_in_times[ticket_number]

    # Remove the check-in record from the file
    filename = "car_information.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("Ticket Number:") and ticket_number in line:
                    # Skip until the next entry
                    while i < len(lines) and line.strip() != "":
                        i += 1
                        if i < len(lines):
                            line = lines[i]
                else:
                    # Write the line to the file
                    file.write(line)
                    i += 1
    except FileNotFoundError:
        pass
def disable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['UM'] * spot_count
    parking_lot_num[floor_choice - 1] = ['UM'] * spot_count
    print(f"Floor {floor_choice} has been disabled.")
def enable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['0'] * spot_count
    parking_lot_num[floor_choice - 1] = parking_lot_num2 [floor_choice - 1]
    print(f"Floor {floor_choice} has been enabled.")
def disable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = 'UM'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = 'UM'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been disabled.")
def enable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = '0'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = '0'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been enabled.")
def save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee):
    if is_plate_number_present_in_file(plate_num):
        print(f"Plate number {plate_num} is already in the saved car information.")
        input("Enter To Continue")
        return
    filename = "car_information.txt"
    file = open(filename, "a")
    try:
        file.write(f"Ticket Number: {ticket_number}\n")
        file.write(f"Plate Number: {plate_num}\n")
        file.write(f"Check-In Time: {check_in_times[ticket_number]}\n")
        file.write(f"Check-Out Time: {check_out_time}\n")
        file.write(f"Payment: {total_fee}\n")
        file.write("\n")
    finally:
        file.close()
def supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale):
    filename = "supervisor_report.txt"
    file = open(filename, "a")

    try:
        now = datetime.now()
        formatted_time = now.strftime("%m-%d %H:%M")
        file.write("\n\n")
        print("Date and time M/D H/M", formatted_time)
        file.write(f"Date and time M/D H/M: {formatted_time}\n")
        file.write(f"Available Parking on Each Floor:\n")
        file.write(f"1st floor: {availableparking_floor1()}\n")
        file.write(f"2nd floor: {availableparking_floor2()}\n")
        file.write(f"3rd floor: {availableparking_floor3()}\n")
        file.write(f"4th floor: {availableparking_floor4()}\n")
        file.write(f"5th floor: {availableparking_floor5()}\n")
        file.write(f"No. of Tickets released: {released_ticket_counter}\n")
        file.write(f"Maximum parking time: {max_parking_time}\n")
        file.write(f"Minimum parking time: {min_parking_time}\n")
        file.write(f"Total Sales: {total_sale:.2f}Php\n")
        file.write(f"Average parking time: {average_parking_time:.5f} minutes\n")
        file.write("\n\n")
    finally:
        file.close()
def report_logs( released_ticket_counter, max_parking_time):
    global min_parking_time  # Assuming min_parking_time is a global variable

    filename = "All report logs.txt"
    file = open(filename, "a")

    try:
        now = datetime.now()
        formatted_time = now.strftime("%m-%d %H:%M")
        file.write("\n")
        print("Date and time M/D H/M", formatted_time)
        file.write(f"Date and time M/D H/M: {formatted_time}\n")
        file.write(f"Available Parking on Each Floor:\n")
        file.write(f"1st floor: {availableparking_floor1()}\n")
        file.write(f"2nd floor: {availableparking_floor2()}\n")
        file.write(f"3rd floor: {availableparking_floor3()}\n")
        file.write(f"4th floor: {availableparking_floor4()}\n")
        file.write(f"5th floor: {availableparking_floor5()}\n")
        file.write(f"No. of Tickets released: {released_ticket_counter}\n")
        file.write(f"Maximum parking time: {max_parking_time or 0}\n")
        file.write(f"Minimum parking time: {min_parking_time or 0}\n")

    finally:
        file.close()
def valid_plate(plate_num):
    plate_num = plate_num.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    if len(plate_num) == 7 and plate_num[:3].isalpha() and plate_num[3:].isdigit():
        return True
    return False
def display_parking_statistics():
    global max_parking_time, min_parking_time,average_parking_time   ####
    if max_parking_time == 0:
        print("No vehicles have parked yet.")
        input("Press Enter To Continue")
    else:
        average_parking_time = total_parking_time / len(check_in_times) if check_in_times else 0
        print(f"Maximum parking time: {max_parking_time} minutes")
        print(f"Minimum parking time: {min_parking_time} minutes")
        print(f"Average parking time: {average_parking_time:.2f} minutes")
        print(f"Total Sale: {total_sale}")
        input("Press Enter To Continue")     
def clear_file_content(filename):
    try:
        file = open(filename, 'w')
        file.truncate(0)
        file.close()
        print(f"Contents of {filename} cleared.")
    except:
        print(f"Error clearing contents of {filename}.")
def design(): #ibahin sana toh
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠴⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠋⠉⠉⠉⠉⠉⠉⠉⠻⠛⠷⣦⡀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣾⣏⣉⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣦⡶⢾⣷⠀⠀⠻⡆⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⣼⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⢛⡿⠭⠿⠿⠿⢿⣿⠀⠀⠀⢿⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣤⡟⢀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⡿⣿⣿⣽⠇⠀⠀⠀⠀⠈⣿⡀⠀⠀⢸⡄⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣀⡀⠀⠀⠈⢁⣿⣧⣴⣿⣿⣶⡶⠶⠶⠶⠿⠿⢶⣶⣦⣤⣤⣴⢗⣇⣀⣠⡤⢤⣶⡒⣺⣭⡽⢷⣄⣀⣠⣧⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣩⢟⣉⡤⠽⢷⣶⣿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣀⣴⢟⣿⠟⠻⢷⣾⣧⠥⡴⠚⣛⣛⣍⣥⠤⠴⠖⠚⣿⠟⠿⣧⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠛⣻⣿⡷⠶⣏⠉⠀⠀⣀⣠⣤⠤⠤⠶⠒⠛⠚⠋⢉⣉⡿⠁⡾⢁⣴⠶⣤⢻⡟⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⣸⠃⣴⣾⣿⣆⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⠚⢿⣶⢦⣿⣷⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣉⡥⠤⠤⠴⠒⠚⠛⠛⠉⠉⠉⣸⠃⢸⢃⡞⠙⣶⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣼⢋⣍⣿⣿⣿")
    print("⠀⠀⠀⠀⢀⣴⢞⡽⠛⣇⠀⠀⢹⣠⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠈⢳⡹⡆⠀⢀⣠⠴⠖⠒⠚⠒⠲⠦⣿⣀⡼⢸⣏⣓⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣿⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⢠⡞⢡⡞⠁⠀⠸⣷⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⣠⣿⣣⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢾⣄⣩⢿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣿⣯⣏⣿⠿⠟")
    print("⠀⠀⠀⣿⠀⡟⠀⠀⠀⠀⢀⠀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣤⡀⠀⠈⠛⠾⣿⣹⠇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⣷⢿⣿⠀⠀")
    print("⠀⠀⠀⣷⠰⠃⠀⣠⠶⣴⡏⢻⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠉⠛⢿⣿⣷⠀⠀⠀⠀⠀⠉⠙⠒⠶⠶⠶⢤⣴⣶⣾⣿⣿⠛⢻⣿⣿⠇⠀⠀")
    print("⣀⣄⡀⠘⣦⠀⠈⢻⣀⣹⢿⣿⣿⡀⠀⢻⣿⣿⣿⠋⠙⣿⣾⡿⠁⠀⠀⠀⠀⠀⠀⣰⡟⢁⣴⣶⣶⡄⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀⣀⣀⣤⠶⠞⠛⠉⠁⠀⠘⠶⠤⠟⠋⠀⠀⠀")
    print("⣿⡙⠓⠲⠾⣷⣶⣤⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣦⣠⠿⠛⠀⠀⠀⠀⠀⠀⠀⣼⠏⣰⡻⣄⣿⣿⣿⠀⢾⣿⣿⣄⣀⣤⠴⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠉⠉⠙⠛⠻⣿⢿⠿⣿⣯⣹⣿⣿⢛⣿⠿⠟⠛⠿⠷⠤⣤⣀⣀⡀⠀⢀⣤⣾⡟⢀⣏⣽⣿⣿⣿⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠹⣾⣷⡏⠉⠙⠛⠛⠿⠿⢿⣷⠶⠤⣤⣀⡀⠀⠀⠉⠉⠉⠙⣿⡇⣼⣿⣿⣿⣿⣿⣻⠃⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠘⠻⠷⣶⣤⣤⣄⣀⣀⠀⠙⡇⠀⠀⠀⠉⠉⠉⠉⠉⢻⠋⢻⡄⢸⣴⣿⣿⣻⣧⠏⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠈⣧⠀⠻⣿⣿⠿⠋⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⡘⢧⣀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("-------------------WELCOME TO ILAO PARKING SOFTWARE-----------------")
def main():
    global plate_num, ticket_number, check_in_times, check_out_time, total_fee
    global released_ticket_counter
    check_out_time = None
    total_fee = None
    while True:
        print("AVAILABLE PARKING SLOTS")
        print (display_parking_lot_num())
        print ("(UM = Under Maintenance) (/ = occupied)")
        print (f"Per Hour: ₱{parking_fee_per_hour}")
        print("---------------------------- Parking Lot Menu ----------------------------")#paltan toh
        print("1. Display available floors")
        print("2. Check-in a vehicle")
        print("3. Check-out and payment")
        print("<<<<<<<<<<< PARKING MAINTENANCE >>>>>>>>>>>")#paltan toh
        print("4. Disable a floor/parking spot")
        print("5. Enable a floor/parking spot")
        print("<<<<<<<<<<< OTHERS >>>>>>>>>>>>>>>>") #paltan toh
        print("6. save current reports")
        print("7. Change parking fee")
        print("8. Display parking statistics")
        print("9. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_parking_lot()
            input ("Press Enter to go Back to Menu")
            clear_screen()
            
        elif choice == "2":
            check_in_vehicle()
            report_logs(released_ticket_counter, max_parking_time)
            clear_screen()
        elif choice == "3":
            check_out()
            
            clear_screen()
        elif choice == "4":
            disable_choice = input("a. Disable parking floor\nb. Disable parking spot\nEnter your choice: ") .lower()
            while disable_choice not in ["a","b"]:
                disable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if disable_choice == "a":
                disable_floor()
                input("Enter To Continue")
                clear_screen()
            elif disable_choice == "b":
                disable_spot()
                input("Enter To Continue")
                clear_screen()
            

        elif choice == "5":
            enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice: ").lower()
            while enable_choice not in ["a","b"]:
                enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if enable_choice == "a":
                enable_floor()
                clear_screen()
            elif enable_choice == "b":
                enable_spot()
                clear_screen()
            

        elif choice == "6":
            #save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee)  # Add code for displaying and saving reports
            if check_in_times:
                average_parking_time = total_parking_time / len(check_in_times)
            else:
                average_parking_time = 0
                supervisor_report(released_ticket_counter,max_parking_time,min_parking_time, average_parking_time,total_sale)
                print("Saving Report")
                time.sleep(1)
                print('saved')
            time.sleep(1)
            clear_screen()
        elif choice == "7":
            change_fee()
            clear_screen()
        elif choice == "8":
            display_parking_statistics()
            clear_screen()
        elif choice == "9":
            if check_in_times:
                average_parking_time = total_parking_time / len(check_in_times)
            else:
                average_parking_time = 0
                supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale)
                clear_file_content("car_information.txt")  # Clear the file content
                print("Saving Report")
            print("Exiting...")
            time.sleep(1)
            print("Have a nice Day")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-9)")

design()
main()

