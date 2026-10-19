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
