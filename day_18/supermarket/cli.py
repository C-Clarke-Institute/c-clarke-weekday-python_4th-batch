from day_18.supermarket.models import SuperMarketError
from day_18.supermarket.repositories import InMemoryProductRepository, InMemoryCustomerRepository, \
    InMemoryOrderRepository
from day_18.supermarket.service import SuperMarketService


supermarket_service = SuperMarketService(
    InMemoryProductRepository(),
    InMemoryCustomerRepository(),
    InMemoryOrderRepository()
)

def add_product():
    try:
        prod_id = input("Enter Product id - : ")
        name = input("Enter product name - : ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))
        supermarket_service.add_product(prod_id,name,price,quantity)
    except SuperMarketError as e:
        print(f"Error - {str(e)}")


def add_a_customer():
    cust_id = input("Enter Customer id : ").strip().lower()
    cust_name = input("Enter Customer Name :  ")
    email = input("Enter Customer Email : " )
    contact = input("Enter Customer contact number : ")

    try :
        supermarket_service.add_customer(cust_id,cust_name,email,contact)

    except SuperMarketError as e :
        print(e)
        return


def view_all_products():
    try:
        products = supermarket_service.product_repository.list_all_products()

        for product in products:
            print(f"Product ID - {product.product_id} | Product Name : {product.name} | "
                  f"Unit Price - {product.price} | Quantity : {product.quantity} ")

    except SuperMarketError as e:
        print(e)

def list_all_customers():
    customers = supermarket_service.customer_repository.list_all_customers()
    if not customers:
        print("No customer found.")
        return
    for customer in customers:
        print(f'ID : {customer.customer_id} | Name : {customer.name} | '
              f'Email : {customer.email} | Phone : {customer.contact_no}')

def add_a_order():
     try:
         list_all_customers()
         order_id = input("Enter order ID : ").strip()
         cust_id = input("Enter Customer ID for this order : ").strip()

         order = supermarket_service.add_order(order_id, cust_id)
         print(f"Order {order.order_id} created for {order.customer_id}")
         add_item_to_order(order_id)

     except SuperMarketError as e:
         print(e)



def add_item_to_order(order_id):

    while True:

        print("\n========================"
              "Available Items"
              "========================")

        view_all_products()

        product_id = input("Enter Product ID (or press Enter to finish : )").strip()

        if not product_id:
            break

        try :
            quantity = float(input("Enter Quantity : "))
            supermarket_service.add_item_to_order(order_id,product_id,quantity)
            print("item added to order.")

        except ValueError:
            print("Quantity must be a number .")

        except SuperMarketError as e:
            print(e)


def view_all_orders():
    orders = supermarket_service.order_repository.list_all_orders()

    if not orders:
        print("No Order found.")
        return

    for order in orders:
        total = sum(item.total_price() for item in order.items)

        print(f"\nOrder : {order.order_id} | Customer : {order.customer_name}"
              f"Total : {total:.2f}")

        for item in order.items:
            print(f"{item.product_name} x {item.quantity}"
                  f" | {item.unit_price:.2f} = {item.total_price():.2f}")

while True:

    print("""
    1) Press 1 to add a product
    2) Press 2 to add a customer
    3) Press 3 to list all products
    4) Press 4 to add a order
    5) Press 5 tp view all orders
    """)

    choice = input("Enter your choice")

    if choice == "1":
        add_product()

    if choice == "2":
        add_a_customer()

    if choice == "3" :
        view_all_products()

    if choice == "4":
        add_a_order()

    if choice == "5":
        view_all_orders()






