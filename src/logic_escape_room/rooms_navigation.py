from src.display.escape_rooms_menu import display_escape_rooms_menu
from src.utils.user_input import num_input, str_input
from src.logic_escape_room.manage_rooms import Add_a_new_room, update_room, enable_or_disable_room
from src.logic_escape_room.view_rooms import view_all_rooms, view_room_by_id

def manage_room_navigation():
    while True:
        display_escape_rooms_menu()
        user_select = num_input("Select a number from the menu: ")
        if user_select == 1:
            view_all_rooms()
        if user_select == 2:
            room_id = num_input("(int) enter room id: ")
            view_room_by_id(room_id)
        if user_select == 3:
            room_name = str_input("(str) enter room name: ")
            difficulty = str_input("(str) enter difficulty: ")
            duration = num_input("(int) enter duration: ")
            min_players = num_input("(int) enter min players: ")
            max_players = num_input("(int) enter max players: ")
            price_per_player = num_input("(int) price per player: ")
            Add_a_new_room(room_name, difficulty, duration, min_players, max_players, price_per_player)
        if user_select == 4:
            room_id = num_input("(int) enter room id: ")
            key = str_input("(str) enter key to update: ")
            value = str_input("(str) enter value to update: ")
            print(update_room(room_id, key, value))
        if user_select == 5:
            room_id = num_input("(int) enter room id: ")
            enable_or_disable_room(room_id)
        if user_select == 0:
            break