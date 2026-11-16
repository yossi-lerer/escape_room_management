from datetime import datetime
from src.logic_order_management.view_orders import view_order_by_id
from src.db.json_handler import get_data_from_json


def is_room_exists_and_is_active(room_id):
    data = get_data_from_json("./src/db/rooms.json")
    for room in data:
        if room["room_id"] == room_id:
            if room["is_active"]:
                return True
    return False

def is_players_at_range(room_id, players):
    data = get_data_from_json("./src/db/rooms.json")
    for room in data:
        if room["room_id"] == room_id:
            if room["min_players"] <= players <=  room["max_players"]:
                return True
    return False
    
def validate_time_at_open_hours(hour):
    FMT = '%H:%M'
    time = datetime.strptime(hour, FMT)
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    if 10 <= hour <= 22:
        if hour == 22 and minute > 0:
            return False
        return True
    return False

def is_room_free_at_time(booking_order_time, new_order_time, game_time):
    FMT = '%H:%M'
    calculate = datetime.strptime(new_order_time, FMT) - datetime.strptime(booking_order_time, FMT)
    diff_in_mins = int(calculate.total_seconds() / 60)

    if diff_in_mins < 0:
        if diff_in_mins + game_time + 15 <= 0:
            return True
    if diff_in_mins > 0:
        if diff_in_mins - game_time - 15 >= 0:
            return True        
    return False

def is_date_is_future(date_string):
    try:
        this_date = datetime.strptime(date_string, '%d-%m-%Y %H:%M')
        now = datetime.today()
        if this_date < now:
            return False
        return True
    except:
        return False
    
def main_validate_booking(game_time):
    customer_name = input("(str) customer_name ")
    room_id = ""
    players = 0
    data = ""
    time = ""

    while not is_room_exists_and_is_active(room_id):
        room_id = input("(R000) room ")

    while not is_players_at_range(room_id, players):
        players = int(input("(int) players "))
    
    while not is_date_is_future(f"{data} {time}"):
        data = input("(10-12-2026) data ")
        time = input("(11:47) time ")

    if not validate_time_at_open_hours(time):
        print("4")
        return False
    
    data_base = get_data_from_json("./src/db/bookings.json")
    for booking in data_base:
        if booking["room_id"] == room_id:
            if booking["booking_date"] == data:
                if not is_room_free_at_time(booking["start_time"], time, game_time):
                    print("5")
                    return False
    return (customer_name, room_id, data, time, players)


    # is_players_at_range("R002", 5)
    # is_date_is_future("16-11-2026 11:47")
    # validate_time_at_open_hours('22:00')
    # is_room_free_at_time('22:00', '20:00', 100)