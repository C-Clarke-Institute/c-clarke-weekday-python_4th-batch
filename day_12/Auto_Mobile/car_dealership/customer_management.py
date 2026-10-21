customer_details = [
    {"cust_id": "001",
     "name": "test",
     "contact" : "07123456789",
     "purchases" :
         [
             {"veh_id" : 5,
              "name" : "Model 3",
              "manufacture_year" : 2020,
              "model" : "Tesla",
              "country_of_origin" : "USA",
              "price" : 45635678.0},

         ]
     }
]

def add_customer(customer):
    if "cust_id" not in customer:
        print("Customer ID is required")
        return

    for cust in customer_details:
        if cust["cust_id"] == customer["cust_id"]:
            print("Customer ID already Exists.")
            return

    customer_details.append(customer)
    print("Customer added Successfully")

def get_customer_by_id(customer_id) :
    #get the customer from the customer list

    for cust in customer_details:
        if cust["cust_id"] == customer_id:
            return cust

    return None

def add_customer_order(cust_id, car_info) :

    if get_customer_by_id(cust_id) is not None:
        for cust in customer_details:
            if cust["cust_id"] == cust_id:
                cust["purchases"].append(car_info)

def view_customer(customer_id) : #display the customer
     customer = get_customer_by_id(customer_id)

     if customer is None:
         print("Customer not found.")
         return
     print("========= Customer Details =========")

     print(f"Customer ID : {customer['cust_id']}")
     print(f"Customer Name : {customer['name']}")
     print(f"Contact : {customer['contact']}")
     print("\nPurchase History")

     if not customer['purchases']:
         print("No purchases yet.")
         return

     else:

         for car in customer["purchases"]:

             print("-" * 30)
             print(f"Vehicle ID : {car['veh_id']}")
             print(f"Name : {car['name']}")
             print(f"Manufacture Year : {car['manufacture_year']}")
             print(f"Model : {car['model']}")
             print(f"Country : {car['model']}")
             print(f"Price : {car['price']}")

