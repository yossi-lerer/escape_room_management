from src.db.json_handler import add_data_to_json, get_data_from_json, update_json

def creating_a_new_order():
    record = {
        "booking_id": "B001",
        "customer_name": "David Cohen",
        "room_id": "R001",
        "booking_date": "2026-11-14",
        "start_time": "10:00",
        "players": 4,
        "total_price": 320.0,
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