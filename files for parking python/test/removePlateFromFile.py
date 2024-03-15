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
