#Super Market Bill

#ask how many products the customer wants to purches
# for each product has  name, quantity , price
# need to show product total

# calculate subtotal

# if subtotal over than 20000 have 20% , over 10000 10% , over 5000 5%

# diaplay welcome note, each product name quantity, price , product totaal,
# subtotal, discount, final bill amount, thank you note


product_count = int(input("How many products : "))

subtotal = 0

for i in range (product_count):

    print(f"\nProduct {i+1}"
          f"---------")

    prod_name = input("Enter Product Name : ")
    prod_quantity = float(input("Enter Product Quantity : "))
    prod_price = float(input("Enter Product Price : "))

    prod_total = prod_price * prod_quantity

    print(f"{prod_name} Total : {prod_total}")

    subtotal += prod_total

print("\n=====================")
if subtotal >= 20000:
    discount_rate = 0.2
elif subtotal >= 10000:
    discount_rate = 0.15
elif subtotal >= 5000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_bill = subtotal - discount

print(f"Subtotal : Rs.{subtotal}"
      f"\nDiscount : Rs.{discount}"
      f"\n======================="
      f"\nFinal Bill amount : {final_bill}"
      f"\n=======================")

print("\n---- Thank You Come Again ----")
