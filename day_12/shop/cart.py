
cart_items = [] #[{"product" : {"id" : 1, "name" : "rice", "price" : 200.00} , "quantity" : 2}]

def add_to_cart(product, quantity):
    cart_items.append({"product": product, "quantity" : quantity })
    print(f"{product['name']} * {quantity} added to cart successfully")

def view_cart():
    for item in cart_items:
        print(f"{item['product']['name']} * {item['quantity']} | "
              f" price = {item['product']['price'] * item['quantity']}")