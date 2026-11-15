from src.display.escape_rooms_menu import display_escape_rooms_menu
from src.utils.user_input import num_input
from src.logic_escape_room.manage_rooms import Add_a_new_room, update_room, enable_or_disable_room
from src.logic_escape_room.view_rooms import view_all_rooms, view_room_by_id

def manage_room_navigation():
    while True:
        display_escape_rooms_menu()
        user_select = num_input("Select a number from the menu: ")
        if user_select == 1:
            view_all_rooms()
        if user_select == 2:
            view_room_by_id("R001")
        if user_select == 3:
            Add_a_new_room("sdf", 2,3,4,5,6)
        if user_select == 4:
            update_room("R001", "difficulty", "easy")
        if user_select == 5:
            enable_or_disable_room("R001")
        if user_select == 0:
            break