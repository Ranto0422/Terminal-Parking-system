# Terminal Parking System

A menu-driven parking lot manager that runs in the terminal. It tracks 5 floors of 16 spots, issues tickets, charges by the hour, lets staff close floors or spots for maintenance, and writes logs and a supervisor report to text files. Built in a team of five in our first year, first term, as a case study for a first-year programming course.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

| | |
|---|---|
| **Stack** | Python 3, standard library only |
| **Concepts** | Lists as a 2D grid, input validation, file I/O, date and time math, menu loop |
| **Team** | Malaluan, Torio, Aba, Garfin, Valdez |

## Features

1. **Live lot map** of all 5 floors, showing free, occupied (`/`) and under maintenance (`UM`) spots
2. **Check-in:** validates the plate number, rejects duplicates, picks floor and spot, and issues a ticket like `F4-S7`
3. **Check-out:** looks up the ticket, computes hours parked and the fee (default ₱40 per hour), and frees the spot
4. **Maintenance:** disable or re-enable a whole floor or a single spot
5. **Change the hourly fee**
6. **Statistics and reports:** tickets released, longest, shortest and average stay, and total sales, saved to `supervisor_report.txt`
7. **Logs:** check-ins are written to `car_information.txt` and `All report logs.txt`

## Running it

```bash
python parking_system.py
```

```
---------------------------- Parking Lot Menu ----------------------------
1. Display available floors
2. Check-in a vehicle
3. Check-out and payment
<<<<<<<<<<< PARKING MAINTENANCE >>>>>>>>>>>
4. Disable a floor/parking spot
5. Enable a floor/parking spot
<<<<<<<<<<< OTHERS >>>>>>>>>>>>>>>>
6. save current reports
7. Change parking fee
8. Display parking statistics
9. Exit Program
```

The report and log `.txt` files are created in the folder you run it from. The screen clear uses the Windows `cls` command; on macOS or Linux the menu still works but the screen will not clear.

## Project structure

```
Terminal-Parking-system/
├── parking_system.py    the version we submitted (single file)
├── modular/             unfinished refactor into modules (does not run yet)
│   ├── main.py
│   ├── parking.py       lot state, check-in, floors and spots
│   ├── utilities.py     fees, check-out, files, reports, validation
│   └── layout.py        screen drawing and the main menu
└── archive/             earlier drafts and small scripts used to test each function
```

`archive/` is kept to show how the project developed. It is not needed to run the program. The `modular/` refactor stopped partway and currently fails with a `SyntaxError` in `utilities.py`; `parking_system.py` is the working version.
