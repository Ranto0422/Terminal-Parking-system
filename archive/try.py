import random
import datetime

class ParkingSpace:
    def __init__(self, floor, capacity):
        self.floor = floor
        self.capacity = capacity
        self.available_spaces = capacity
        self.locked_down = False

class Car:
    def __init__(self, plate_number, check_in_time, ticket_number):
        self.plate_number = plate_number
        self.check_in_time = check_in_time
        self.ticket_number = ticket_number

def generate_ticket_number():
    return random.randint(1000, 9999)

def calculate_parking_fee(check_in_time, check_out_time, rate_per_hour=40):
    hours_parked = (check_out_time - check_in_time).seconds // 3600
    return hours_parked * rate_per_hour

def main():
    floors = [ParkingSpace(floor, 16) for floor in range(1, 6)]
    cars = []
    parking_rate = 40  # Initial parking rate per hour
    released_tickets = []
    total_sales = 0
    parking_times = []
    
    while True:
        print("\nOptions:")
        print("1. Park a car")
        print("2. Check out a car")
        print("3. Adjust parking rate")
        print("4. Reports")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            # Park a car
            available_floors = [floor for floor in floors if not floor.locked_down and floor.available_spaces > 0]
            if not available_floors:
                print("No available parking space.")
                continue

            floor = random.choice(available_floors)
            plate_number = input("Enter car plate number: ")
            check_in_time = datetime.datetime.now()
            ticket_number = generate_ticket_number()
            car = Car(plate_number, check_in_time, ticket_number)

            floor.available_spaces -= 1
            cars.append(car)
            print(f"Car parked on Floor {floor.floor}, Ticket Number: {ticket_number}")

        elif choice == "2":
            # Check out a car
            ticket_number = int(input("Enter parking ticket number: "))
            for car in cars:
                if car.ticket_number == ticket_number:
                    check_out_time = datetime.datetime.now()
                    parking_time = check_out_time - car.check_in_time
                    parking_fee = calculate_parking_fee(car.check_in_time, check_out_time, parking_rate)
                    print(f"Car with Plate Number {car.plate_number} is checking out.")
                    print(f"Parking Time: {parking_time}, Parking Fee: {parking_fee} pesos")
                    cars.remove(car)
                    floor.available_spaces += 1
                    released_tickets.append(ticket_number)
                    total_sales += parking_fee
                    parking_times.append(parking_time)
                    break
            else:
                print("Ticket number not found.")
        
        elif choice == "3":
            # Adjust parking rate
            new_rate = int(input("Enter new parking rate per hour: "))
            parking_rate = new_rate
            print(f"Parking rate updated to {new_rate} pesos per hour.")
        
        elif choice == "4":
            # Reports
            print(f"No. of Available Parking Spaces per Floor:")
            for floor in floors:
                print(f"Floor {floor.floor}: {floor.available_spaces} spaces")

            print(f"No. of Released Tickets: {len(released_tickets)}")

            if parking_times:
                max_parking_time = max(parking_times)
                min_parking_time = min(parking_times)
                average_parking_time = sum(parking_times, datetime.timedelta()) / len(parking_times)
                print(f"Maximum Parking Time: {max_parking_time}")
                print(f"Minimum Parking Time: {min_parking_time}")
                print(f"Average Parking Time: {average_parking_time}")

            print(f"Total Sales: {total_sales} pesos")

        elif choice == "5":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
