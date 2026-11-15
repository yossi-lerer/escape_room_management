from src.display.start_system import show_start_system_msg
from src.logic_order_management.order_navigation import manage_order_navigation
from src.logic_escape_room.rooms_navigation import manage_room_navigation


def main():
    while True:
        show_start_system_msg()
        user_select = input("Select a number from the menu: ")
        user_select = int(user_select)
        if user_select == 1:
            manage_room_navigation()
        elif user_select == 2:
            manage_order_navigation()
        elif user_select == 3:
            break
if __name__ == "__main__":
    main()