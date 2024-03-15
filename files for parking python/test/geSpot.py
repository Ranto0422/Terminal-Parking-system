def get_spot_choice():
    while True:
        spot_choice = input("Enter desired parking spot (1-16): ")
        if spot_choice.isnumeric() and 1 <= int(spot_choice) <= spot_count:
            return int(spot_choice)
        print("Entered parking spot does not exist.")
