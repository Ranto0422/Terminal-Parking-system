def enable_spot():
    floor_choice = get_floor_choice()
    spot_choice = get_spot_choice()
    parking_lot[floor_choice - 1][spot_choice - 1] = '0'
    parking_lot_num[floor_choice - 1][spot_choice - 1] = '0'
    print(f"Spot {spot_choice} on Floor {floor_choice} has been enabled.")
