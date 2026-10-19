def display_parking_lot_num():
    floor_number = 1
    for floor in parking_lot_num:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1 
