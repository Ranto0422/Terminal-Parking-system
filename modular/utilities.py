import time
from datetime import datetime
released_ticket_counter = 0

check_in_times = {}
parking_fee_per_hour = 40

total_sale=0

max_parking_time = 0
min_parking_time = float('inf')
total_parking_time = 0

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