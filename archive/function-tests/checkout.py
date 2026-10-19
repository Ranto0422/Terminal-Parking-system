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
