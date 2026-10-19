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
