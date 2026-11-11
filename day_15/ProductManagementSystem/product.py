
# Create a Product class:
# attribute - product name, price , quantity
#methods - display_product(), calculate_total_value(), sell()



class Product:

    def __init__(self, prod_name : str, quantity : float , price : float):

        self.product_name  = prod_name
        self.quantity = quantity
        self.price = price

    def display_product(self):
        print("\n----------------")
        print(f"\nProduct Name : {self.product_name}"
              f"\nPrice : {self.price}"
              f"\nQuantity : {self.quantity}")

    def cal_total_value(self):
        return self.quantity * self.price

    def sell(self, selling_quantity : float):

        if selling_quantity <= 0:
            print('Invalid Qunatity')

        elif selling_quantity > self.quantity:
            print("Insufficent Stock !")
            print(f"Available stock : {self.quantity}" )

        else:
            self.quantity -= selling_quantity
            print(f"{selling_quantity} items sold successfully ")


prod1 = Product("ABC", 89, 100)

prod2 = Product("test", 10,12.)

prod2.sell(6)
prod1.display_product()

