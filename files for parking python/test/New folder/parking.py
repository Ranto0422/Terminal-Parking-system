def clear_screen():
    os.system('cls')
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
def save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee):
    if is_plate_number_present_in_file(plate_num):
        print(f"Plate number {plate_num} is already in the saved car information.")
        input("Enter To Continue")
        return
    filename = "car_information.txt"
    file = open(filename, "a")
    try:
        file.write(f"Ticket Number: {ticket_number}\n")
        file.write(f"Plate Number: {plate_num}\n")
        file.write(f"Check-In Time: {check_in_times[ticket_number]}\n")
        file.write(f"Check-Out Time: {check_out_time}\n")
        file.write(f"Payment: {total_fee}\n")
        file.write("\n")
    finally:
        file.close()
def supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale):
    filename = "supervisor_report.txt"
    file = open(filename, "a")

    try:
        now = datetime.now()
        formatted_time = now.strftime("%m-%d %H:%M")
        file.write("\n\n")
        print("Date and time M/D H/M", formatted_time)
        file.write(f"Date and time M/D H/M: {formatted_time}\n")
        file.write(f"Available Parking on Each Floor:\n")
        file.write(f"1st floor: {availableparking_floor1()}\n")
        file.write(f"2nd floor: {availableparking_floor2()}\n")
        file.write(f"3rd floor: {availableparking_floor3()}\n")
        file.write(f"4th floor: {availableparking_floor4()}\n")
        file.write(f"5th floor: {availableparking_floor5()}\n")
        file.write(f"No. of Tickets released: {released_ticket_counter}\n")
        file.write(f"Maximum parking time: {max_parking_time}\n")
        file.write(f"Minimum parking time: {min_parking_time}\n")
        file.write(f"Total Sales: {total_sale:.2f}Php\n")
        file.write(f"Average parking time: {average_parking_time:.5f} minutes\n")
        file.write("\n\n")
    finally:
        file.close()
def report_logs( released_ticket_counter, max_parking_time):
    global min_parking_time  # Assuming min_parking_time is a global variable

    filename = "All report logs.txt"
    file = open(filename, "a")

    try:
        now = datetime.now()
        formatted_time = now.strftime("%m-%d %H:%M")
        file.write("\n")
        print("Date and time M/D H/M", formatted_time)
        file.write(f"Date and time M/D H/M: {formatted_time}\n")
        file.write(f"Available Parking on Each Floor:\n")
        file.write(f"1st floor: {availableparking_floor1()}\n")
        file.write(f"2nd floor: {availableparking_floor2()}\n")
        file.write(f"3rd floor: {availableparking_floor3()}\n")
        file.write(f"4th floor: {availableparking_floor4()}\n")
        file.write(f"5th floor: {availableparking_floor5()}\n")
        file.write(f"No. of Tickets released: {released_ticket_counter}\n")
        file.write(f"Maximum parking time: {max_parking_time or 0}\n")
        file.write(f"Minimum parking time: {min_parking_time or 0}\n")

    finally:
        file.close()
def valid_plate(plate_num):
    plate_num = plate_num.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    if len(plate_num) == 7 and plate_num[:3].isalpha() and plate_num[3:].isdigit():
        return True
    return False
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
def clear_file_content(filename):
    try:
        file = open(filename, 'w')
        file.truncate(0)
        file.close()
        print(f"Contents of {filename} cleared.")
    except:
        print(f"Error clearing contents of {filename}.")
def design(): #ibahin sana toh
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠴⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠋⠉⠉⠉⠉⠉⠉⠉⠻⠛⠷⣦⡀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣾⣏⣉⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣦⡶⢾⣷⠀⠀⠻⡆⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⣼⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⢛⡿⠭⠿⠿⠿⢿⣿⠀⠀⠀⢿⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣤⡟⢀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⡿⣿⣿⣽⠇⠀⠀⠀⠀⠈⣿⡀⠀⠀⢸⡄⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣀⡀⠀⠀⠈⢁⣿⣧⣴⣿⣿⣶⡶⠶⠶⠶⠿⠿⢶⣶⣦⣤⣤⣴⢗⣇⣀⣠⡤⢤⣶⡒⣺⣭⡽⢷⣄⣀⣠⣧⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣩⢟⣉⡤⠽⢷⣶⣿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣀⣴⢟⣿⠟⠻⢷⣾⣧⠥⡴⠚⣛⣛⣍⣥⠤⠴⠖⠚⣿⠟⠿⣧⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠛⣻⣿⡷⠶⣏⠉⠀⠀⣀⣠⣤⠤⠤⠶⠒⠛⠚⠋⢉⣉⡿⠁⡾⢁⣴⠶⣤⢻⡟⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⣸⠃⣴⣾⣿⣆⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⠚⢿⣶⢦⣿⣷⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣉⡥⠤⠤⠴⠒⠚⠛⠛⠉⠉⠉⣸⠃⢸⢃⡞⠙⣶⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣼⢋⣍⣿⣿⣿")
    print("⠀⠀⠀⠀⢀⣴⢞⡽⠛⣇⠀⠀⢹⣠⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠈⢳⡹⡆⠀⢀⣠⠴⠖⠒⠚⠒⠲⠦⣿⣀⡼⢸⣏⣓⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣿⣿⣿⣿⣿⣿")
    print("⠀⠀⠀⢠⡞⢡⡞⠁⠀⠸⣷⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⣠⣿⣣⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢾⣄⣩⢿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣿⣯⣏⣿⠿⠟")
    print("⠀⠀⠀⣿⠀⡟⠀⠀⠀⠀⢀⠀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣤⡀⠀⠈⠛⠾⣿⣹⠇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⣷⢿⣿⠀⠀")
    print("⠀⠀⠀⣷⠰⠃⠀⣠⠶⣴⡏⢻⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠉⠛⢿⣿⣷⠀⠀⠀⠀⠀⠉⠙⠒⠶⠶⠶⢤⣴⣶⣾⣿⣿⠛⢻⣿⣿⠇⠀⠀")
    print("⣀⣄⡀⠘⣦⠀⠈⢻⣀⣹⢿⣿⣿⡀⠀⢻⣿⣿⣿⠋⠙⣿⣾⡿⠁⠀⠀⠀⠀⠀⠀⣰⡟⢁⣴⣶⣶⡄⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀⣀⣀⣤⠶⠞⠛⠉⠁⠀⠘⠶⠤⠟⠋⠀⠀⠀")
    print("⣿⡙⠓⠲⠾⣷⣶⣤⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣦⣠⠿⠛⠀⠀⠀⠀⠀⠀⠀⣼⠏⣰⡻⣄⣿⣿⣿⠀⢾⣿⣿⣄⣀⣤⠴⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠉⠉⠙⠛⠻⣿⢿⠿⣿⣯⣹⣿⣿⢛⣿⠿⠟⠛⠿⠷⠤⣤⣀⣀⡀⠀⢀⣤⣾⡟⢀⣏⣽⣿⣿⣿⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠹⣾⣷⡏⠉⠙⠛⠛⠿⠿⢿⣷⠶⠤⣤⣀⡀⠀⠀⠉⠉⠉⠙⣿⡇⣼⣿⣿⣿⣿⣿⣻⠃⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠘⠻⠷⣶⣤⣤⣄⣀⣀⠀⠙⡇⠀⠀⠀⠉⠉⠉⠉⠉⢻⠋⢻⡄⢸⣴⣿⣿⣻⣧⠏⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠈⣧⠀⠻⣿⣿⠿⠋⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⡘⢧⣀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("-------------------WELCOME TO ILAO PARKING SOFTWARE-----------------")
def main():
    global plate_num, ticket_number, check_in_times, check_out_time, total_fee
    global released_ticket_counter
    check_out_time = None
    total_fee = None
    while True:
        print("AVAILABLE PARKING SLOTS")
        print (display_parking_lot_num())
        print ("(UM = Under Maintenance) (/ = occupied)")
        print (f"Per Hour: ₱{parking_fee_per_hour}")
        print("---------------------------- Parking Lot Menu ----------------------------")#paltan toh
        print("1. Display available floors")
        print("2. Check-in a vehicle")
        print("3. Check-out and payment")
        print("<<<<<<<<<<< PARKING MAINTENANCE >>>>>>>>>>>")#paltan toh
        print("4. Disable a floor/parking spot")
        print("5. Enable a floor/parking spot")
        print("<<<<<<<<<<< OTHERS >>>>>>>>>>>>>>>>") #paltan toh
        print("6. save current reports")
        print("7. Change parking fee")
        print("8. Display parking statistics")
        print("9. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_parking_lot()
            input ("Press Enter to go Back to Menu")
            clear_screen()
            
        elif choice == "2":
            check_in_vehicle()
            report_logs(released_ticket_counter, max_parking_time)
            clear_screen()
        elif choice == "3":
            check_out()
            
            clear_screen()
        elif choice == "4":
            disable_choice = input("a. Disable parking floor\nb. Disable parking spot\nEnter your choice: ") .lower()
            while disable_choice not in ["a","b"]:
                disable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if disable_choice == "a":
                disable_floor()
                input("Enter To Continue")
                clear_screen()
            elif disable_choice == "b":
                disable_spot()
                input("Enter To Continue")
                clear_screen()
            

        elif choice == "5":
            enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice: ").lower()
            while enable_choice not in ["a","b"]:
                enable_choice = input("a. Enable parking floor\nb. Enable parking spot\nEnter your choice A or Bs: ").lower()
            if enable_choice == "a":
                enable_floor()
                clear_screen()
            elif enable_choice == "b":
                enable_spot()
                clear_screen()
            

        elif choice == "6":
            #save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee)  # Add code for displaying and saving reports
            if check_in_times:
                average_parking_time = total_parking_time / len(check_in_times)
            else:
                average_parking_time = 0
                supervisor_report(released_ticket_counter,max_parking_time,min_parking_time, average_parking_time,total_sale)
                print("Saving Report")
                time.sleep(1)
                print('saved')
            time.sleep(1)
            clear_screen()
        elif choice == "7":
            change_fee()
            clear_screen()
        elif choice == "8":
            display_parking_statistics()
            clear_screen()
        elif choice == "9":
            if check_in_times:
                average_parking_time = total_parking_time / len(check_in_times)
            else:
                average_parking_time = 0
                supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale)
                clear_file_content("car_information.txt")  # Clear the file content
                print("Saving Report")
            print("Exiting...")
            time.sleep(1)
            print("Have a nice Day")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-9)")
