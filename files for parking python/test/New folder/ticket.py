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
