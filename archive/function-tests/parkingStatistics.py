def display_parking_statistics():
    global max_parking_time, min_parking_time,average_parking_time   ####
    if max_parking_time == 0:
        print("No vehicles have parked yet.")
        input("Press Enter To Continue")
    else:
        average_parking_time = total_parking_time / len(check_in_times) if check_in_times else 0
        print(f"Maximum parking time: {max_parking_time} minutes")
        print(f"Minimum parking time: {min_parking_time} minutes")
        print(f"Average parking time: {average_parking_time:.2f} minutes")
        print(f"Total Sale: {total_sale}")
        input("Press Enter To Continue")  
