
products = [
    {"id" : 1, "name" : "rice", "price" : 200.00},
    {"id" : 2, "name" : "dhal", "price" : 100.00}
]

def show_products():
    print("Available Products")
    for product in products:
        print(f"{product['id']} | {product['name']} | {product['price']}")

def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

if __name__ == "__main__":
    show_products()
    print(find_product_by_id(2))
