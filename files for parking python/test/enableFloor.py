def enable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['0'] * spot_count
    parking_lot_num[floor_choice - 1] = parking_lot_num2 [floor_choice - 1]
    print(f"Floor {floor_choice} has been enabled.")
