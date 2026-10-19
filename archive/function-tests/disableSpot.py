def disable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = 'UM'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = 'UM'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been disabled.")
