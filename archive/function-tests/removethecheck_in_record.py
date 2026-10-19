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
