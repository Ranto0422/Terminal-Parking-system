def extract_floor_and_spot(ticket_number):
    # Extract the floor and spot numbers from the ticket
    floor_str, spot_str = ticket_number[1:].split("-S")
    floor = int(floor_str)
    spot = int(spot_str)
    return floor, spot
