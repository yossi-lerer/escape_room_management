from src.db.json_handler import add_data_to_json, get_data_from_json, update_json

def Add_a_new_room(name, difficulty, duration, min_players, max_players, price_per_player):
    record = {
        "room_id": generate_room_id(),
        "name": name,
        "difficulty": difficulty,
        "duration": duration,
        "min_players": min_players,
        "max_players": max_players,
        "price_per_player": price_per_player,
        "is_active": True
    }
    add_data_to_json("./src/db/rooms.json", record)
    return

def generate_room_id():
    return 984

def update_room():
    pass

def enable_or_disable_room(room_id):
    data = get_data_from_json("./src/db/rooms.json")
    for record in data:
        if record["room_id"] == room_id:
            if record["is_active"] == True:
                record["is_active"] = False
            else:
                record["is_active"] = True
        update_json("./src/db/rooms.json", data)