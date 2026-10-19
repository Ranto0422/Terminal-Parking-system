def valid_plate(plate_num):
    plate_num = plate_num.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    if len(plate_num) == 7 and plate_num[:3].isalpha() and plate_num[3:].isdigit():
        return True
    return False
