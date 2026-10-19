def get_floor_choice():
    display_parking_lot_num()
    while True:
        floor_choice = input("Enter desired floor (1-5): ")
        if floor_choice.isnumeric() and 1 <= int(floor_choice) <= floor_count:
            return int(floor_choice)
        print("Entered floor does not exist.")
