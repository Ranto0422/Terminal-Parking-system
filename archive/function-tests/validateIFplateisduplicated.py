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
    
