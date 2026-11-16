from src.db.json_handler import add_data_to_json, get_data_from_json, update_json
from src.logic_order_management.validate_booking import get_data_from_json, is_date_is_future, is_players_at_range, is_room_exists_and_is_active, is_room_free_at_time, validate_time_at_open_hours
def creating_a_new_order(data):
    record = {
        "booking_id": f"B{len(get_data_from_json(file_path='./src/db/bookings.json')) + 1:03d}",
        "customer_name": data[0],
        "room_id": data[1],
        "booking_date": data[2],
        "start_time": data[3],
        "players": data[4],
        "total_price": 500,
        "status": "Active",
        "cancellation_fee": 0.0
    }

    add_data_to_json("./src/db/bookings.json", record)
    return

def edit_existing_order(booking_id, key, value):
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        if record["booking_id"] == booking_id:
            record[key] = value
        update_json("./src/db/bookings.json", data)

def cancel_an_order(booking_id):
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        if record["booking_id"] == booking_id:
            record["status"] = "Cancelled"
        update_json("./src/db/bookings.json", data)