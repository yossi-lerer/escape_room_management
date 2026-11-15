from src.db.json_handler import get_data_from_json

def view_all_orders():
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        for key, value in record.items():
            print(f"{key}: {value}")
        print("\n==============================================")

def view_order_by_id(order_id):
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        if record["room_id"] == order_id:
            for key, value in record.items():
                print(f"{key}: {value}")

def view_orders_by_customer(customer_name):
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        if record["customer_name"] == customer_name:
            for key, value in record.items():
                print(f"{key}: {value}")
                
def view_orders_by_date(booking_date):
    data = get_data_from_json("./src/db/bookings.json")
    for record in data:
        if record["booking_date"] == booking_date:
            for key, value in record.items():
                print(f"{key}: {value}")

