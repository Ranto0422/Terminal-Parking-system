def display_parking_lot():
    floor_number = 1
    for floor in parking_lot:
        print(f"Floor {floor_number}: {' '.join(floor)}")
        floor_number += 1
