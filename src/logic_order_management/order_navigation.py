from src.display.order_management_menu import show_order_management_menu
from src.utils.user_input import num_input
from src.logic_order_management.view_orders import view_all_orders, view_order_by_id, view_orders_by_customer, view_orders_by_date
from src.logic_order_management.manage_orders import creating_a_new_order, edit_existing_order, cancel_an_order
from src.logic_order_management.validate_booking import main_validate_booking

def manage_order_navigation():
    while True:
        show_order_management_menu()
        user_select = num_input("Select a number from the menu: ")
        if user_select == 1:
            data = main_validate_booking(30)
            creating_a_new_order(data)
        if user_select == 2:
            view_all_orders()
        if user_select == 3:
            booking_id = "B001"
            view_order_by_id(booking_id)
        if user_select == 4:
            customer_name = "Moshe Israel"
            view_orders_by_customer(customer_name)
        if user_select == 5:
            booking_date = "2026-11-14"
            view_orders_by_date(booking_date)
        if user_select == 6:
            edit_existing_order("B001", "players", 5)
        if user_select == 7:
            cancel_an_order("B001")
        if user_select == 0:
            break