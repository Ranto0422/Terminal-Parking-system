def disable_floor():
    floor_choice = get_floor_choice()
    parking_lot[floor_choice - 1] = ['UM'] * spot_count
    parking_lot_num[floor_choice - 1] = ['UM'] * spot_count
    print(f"Floor {floor_choice} has been disabled.")
