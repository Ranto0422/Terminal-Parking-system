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
