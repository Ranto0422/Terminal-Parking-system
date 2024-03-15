def get_plate_number_from_file(ticket_number):
    filename = "car_information.txt"
    with open(filename, "r") as file:
        for line in file:
            if line.startswith("Ticket Number:") and ticket_number in line:
                # Assuming the plate number is on the line after "Ticket Number:"
                return next(file).strip().split(":")[1].strip()
    return None
