def availableparking_floor1():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_1[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}: Available Parking space in 1st floor")
    Tavailable = Favailable + Tavailable
def availableparking_floor2():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_2[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 2nd floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor3():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_3[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 3rd floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor4():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_4[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 4th floor")
    Tavailable=Favailable+Tavailable
def availableparking_floor5():
    Favailable = 0
    counter = 0
    while counter <= 15:
        if floor_5[counter] == "0":
            Favailable = Favailable + 1
        counter = counter + 1
    return Favailable
    print(f"{Favailable}:Available Parking space in 5th floor")
    Tavailable=Favailable+Tavailable
    print(f"total available slot:{Tavailable}")
def display_parking_lot_num():
    floor_number = 1
    for floor in parking_lot_num:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1    
def display_parking_lot():
    floor_number = 1
    for floor in parking_lot:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1
def disable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['UM'] * spot_count
    parking_lot_num[floor_choice - 1] = ['UM'] * spot_count
    print(f"Floor {floor_choice} has been disabled.")
def enable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['0'] * spot_count
    parking_lot_num[floor_choice - 1] = parking_lot_num2 [floor_choice - 1]
    print(f"Floor {floor_choice} has been enabled.")
def disable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = 'UM'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = 'UM'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been disabled.")
def enable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = '0'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = '0'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been enabled.")
