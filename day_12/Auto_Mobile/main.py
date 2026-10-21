from day_12.Auto_Mobile.car_dealership.customer_management import add_customer, view_customer

while True :
    print("------ CC AutoMobile ------ ")
    print("\n1.Add Customer"
          "2. View All customers"
          "3. View Customer by id ")
    user_input = int(input("Select Menu Number :").strip())

    if user_input == 1 :

        customer_id = input("Enter customer ID : ")
        name = input("Enter Customer Name : ")
        contact = input("Enter Contact Name : ")

        customer = {"cust_id": customer_id,
             "name": name,
             "contact": contact,
             "purchases":[]
             }


        add_customer(customer)

    if user_input == 2 :
        customer_id = input("Enter Customer ID : ")
        view_customer(customer_id)

    if user_input == :
