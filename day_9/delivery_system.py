# create a simple delivery management system
# this system should allow users to
# 1. Create an order
# 2. Calculate delivery charges
# 3. Update delivery status
# 4. View all orders
# 5. Search for an order
# 6. exit
# order informance - order_id , customer_name , Distance, Order_value,
# delivery status
#use lists for storge data
# delivery charges -
# 0 - 5 km - 200 lkr
# more than 5 - 10 350lkr
# more than 10 - 20 500 lkr
# more than 20 - 700 lkr
# if the order value is 10000 or more geet free delivey
# delivery status - preparing, out for delivery, delivered , canceled

orders = []
order_count = 0

def create_order():
    global order_count
    order_count += 1 # order_count = order_count + 1
    order_id = f"ORD{order_count:03d}"
    customer_name = input("Enter Customer Name : ")
    distance = float(input("Enter the distance : "))
    order_value = float(input("Enter the Order value (LKR) : "))

    order = {
        "order_id" : order_id,
        "customer_name" : customer_name,
        "distance" : distance,
        "order_value" : order_value,
        "delivery_charge" : 0,
        "status": "preparing"
    }

    orders.append(order)

    print("\nOrder Created Successfully.")
    print(f"Order ID : {order_id}")

def calculate_delivery_charge(order):

    if order["order_value"] >= 10000:
        return 0

    if order["distance"] <= 5:
        return 200
    elif order["distance"] <= 10:
        return 350
    elif order["distance"] <= 20:
        return 500
    else:
        return 700

def update_delivery_status():

    order_id = input("Enter Order ID : ")

    for order in orders:
        if order_id == order["order_id"]:
            print("\n1. Preparing"
                  "\n2. Out for Delivery"
                  "\n3.Delivered"
                  "\n4.Cancel")
        choice = input("Select status (1- 4) : ")

        if choice == "1":
            order["status"] = "preparing"

        elif choice == "2":
            order["status"] = "Out for delivery ."

        elif choice == "3":
            order["status"] = "Delivered"

        elif choice == "4":
            order["status"] = "Cancelled"

        else:
            print("Invalid Option")
            return

        print("Delivery Status updated ! ")

    print("Order not found . ")

def view_all_orders():

    if len(orders) == 0 :
        print("No Orderes Avilable.")

    for order in orders :
        charge = calculate_delivery_charge(order)
        order["delivery_charge"] = charge

        print("\n")
        print("-" * 75)

        print(f"Order ID : {order['order_id']}")
        print(f"Customer Name : {order['customer_name']}")
        print(f"Distance : {order['distance']}")
        print(f"Order Value : {order['order_alue']}")
        print(f"Delivery Charge : {order['delivery_charge']}")
        print(f"Status : {order['status']}")
        print("-" * 75)

#def search_order():

while True:

    print("\n===== Delivery Management System =====")
    print("\n1. Create a Order"
          "\n2. Calculate Delivery charge"
          "\n3. Update Delivery status"
          "\n4. View all orders."
          "\n5. Search Order"
          "\n6. Exit")

    user_input = input("Enter Menu Number : ")

    if user_input == "1":
        create_order()
    elif user_input == "2":
        order_id = input("Enter Order ID : ")

        for order in orders :

            if order['order_id'] == order_id:
                charge = calculate_delivery_charge(order)
                order['delivery_charge'] = charge

                print(f"Delivery Charge : Rs. {charge}")
                break
            else:
                print("Order not found!")
    elif user_input == "3":
        update_delivery_status()

    elif user_input == "4":
        view_all_orders()

    elif user_input == "5":
        pass

    elif user_input == "6":
        break

    else:
        print("Invalid Input | Try again ")





