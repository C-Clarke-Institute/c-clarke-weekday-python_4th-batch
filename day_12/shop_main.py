from shop import products,billing,cart



while True:

    choice = input("""press 1 to view products
                      press 2 to add products""")

    if choice == "1":
        products.show_products()
