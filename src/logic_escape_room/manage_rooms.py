from src.db.json_handler import add_data_to_json, get_data_from_json, update_json

def Add_a_new_room(name, difficulty, duration, min_players, max_players, price_per_player):
    record = {
        "room_id": f"R{len(get_data_from_json(file_path='./src/db/rooms.json')) + 1:03d}",
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

def update_room(room_id, key, value):
    data = get_data_from_json("./src/db/rooms.json")
    room_id = f"R{room_id:03d}"
    try:
        for record in data:
            if record["room_id"] == room_id:
                record[key]
                record[key] = value
                update_json("./src/db/rooms.json", data)
                return record
        
    except:
        return "key not found"
    
def enable_or_disable_room(room_id):
    data = get_data_from_json("./src/db/rooms.json")
    room_id = f"R{room_id:03d}"
    for record in data:
        if record["room_id"] == room_id:
            if record["is_active"] == True:
                record["is_active"] = False
            else:
                record["is_active"] = True
        update_json("./src/db/rooms.json", data)