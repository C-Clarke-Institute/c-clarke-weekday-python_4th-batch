customer_details = [
    {"cust_id": "001",
     "name": "test",
     "contact" : "07123456789",
     "purchase" :
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

    for cust in customer_details:
        if cust["cust_id"] == customer_id:
            return cust

    return None

def add_customer_order(cust_id, car_info) :

    if get_customer_by_id(cust_id) is not None:
        for cust in customer_details:
            if cust["cust_id"] == cust_id:
                cust["purchases"].append(car_info)