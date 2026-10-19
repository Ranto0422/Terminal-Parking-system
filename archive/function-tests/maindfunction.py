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
