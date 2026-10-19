import time
import os
from datetime import datetime
floor_count = 5
spot_count = 16
released_ticket_counter = 0

check_in_times = {}
parking_fee_per_hour = 40

total_sale=0

max_parking_time = 0
min_parking_time = float('inf')
total_parking_time = 0

floor_1 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_2 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_3 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_4 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_5 = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
floor_1 = ["0"] * 16
floor_2 = ["0"] * 16
floor_3 = ["0"] * 16
floor_4 = ["0"] * 16
floor_5 = ["0"] * 16
parking_lot = [floor_1,floor_2,floor_3,floor_4,floor_5]
ticket=("F1","F2","F3","F4","F5")

A = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
B = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
C = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
D = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
E = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
parking_lot_num = [A,B,C,D,E]

fL1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL4 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
fL5 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
parking_lot_num2 = [fL1,fL2,fL3,fL4,fL5]

Tavailable = 0

def clear_screen():
    os.system('cls')

def availableparking_floor1():
    show_availparking.availableparking_floor1()
    show_availparking.availableparking_floor2()
    show_availparking.availableparking_floor3()
    show_availparking.availableparking_floor4()
    show_availparking.availableparking_floor5()
def change_fee():
    changeTheFee.change_fee()
def display_parking_lot_num():
    displayparkingwithnumbers.display_parking_lot_num()
def display_parking_lot():
    displayparkinglot.display_parking_lot()
def check_in_vehicle():
    checkin.check_in_vehicle()
def is_plate_number_present_in_file():
    validateIFplateisduplicated.is_plate_number_present_in_file()
def get_floor_choice():
    getFloorChoice.get_floor_choice()
def get_spot_choice():
    geSpot.get_spot_choice()
def check_out():
    checkout.check_out()
def get_plate_number_from_file():
    lookforplatenumINfile.get_plate_number_from_file()
def remove_plate_number():
    removePlateFromFile.remove_plate_number()
def extract_floor_and_spot():
    getTheFloorSpotFromTicket.extract_floor_and_spot()
def remove_check_in_record():
    removethecheck_in_record.remove_check_in_record(ticket_number)
def disable_floor():
    disableFloor.disable_floor()
def enable_floor():
    enableFloor.enable_floor()
def disable_spot():
    disableSpot.disable_spot()
def enable_spot():
    enableSpot.enable_spot()
def save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee):
    PlateNumValidation.save_car_information(plate_num, ticket_number, check_in_times, check_out_time, total_fee)
def supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale):
    superVisorReport.supervisor_report(released_ticket_counter, max_parking_time, min_parking_time, average_parking_time, total_sale)
def report_logs( released_ticket_counter, max_parking_time):
    PrintLOGS.report_logs( released_ticket_counter, max_parking_time)
def valid_plate(plate_num):
    platenumberInputValidation.valid_plate(plate_num)
def display_parking_statistics():
    parkingStatistics.display_parking_statistics()
def clear_file_content(filename):
    clearcontentOFfile.clear_file_content(filename)
def design(): #ibahin sana toh
    design.design
def main():
    maindfunction.main()

design()
main()






    
