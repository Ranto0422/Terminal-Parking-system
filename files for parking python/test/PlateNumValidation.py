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
