from src.db.json_handler import get_data_from_json

def view_all_rooms():
    data = get_data_from_json("./src/db/rooms.json")
    for record in data:
        for key, value in record.items():
            print(f"{key}: {value}")
        print("\n==============================================")

def view_room_by_id(room_id):
    data = get_data_from_json("./src/db/rooms.json")
    for record in data:
        if record["booking_id"] == room_id:
            for key, value in record.items():
                print(f"{key}: {value}")