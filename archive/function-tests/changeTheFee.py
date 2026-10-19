def change_fee():
    global parking_fee_per_hour
    
    while True:
        new_fee = input("Enter the new parking fee per hour (input 'Q' to quit): ").strip().upper()
        
        if new_fee == 'Q':
            print("Exiting fee change process.")
            break
        
        if new_fee.isnumeric():
            new_fee = float(new_fee)
            if new_fee >= 0:
                parking_fee_per_hour = new_fee
                print("Parking fee updated successfully.")
                input("Enter To Continue")
                break  # Exit the loop after updating the fee
            else:
                print("Invalid fee. Fee must be a non-negative number.")
        else:
            print("Invalid input. Please enter a valid number for the fee.")
