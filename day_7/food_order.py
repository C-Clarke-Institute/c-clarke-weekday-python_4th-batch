# create a simple food ordering system using list (dont use dictionaries)
# you need to store available foods and their prices.
#display the food menu with price
#ask the customer to select a food from the menu by entering food number
#. add the selected foods in to a order .
#until the customer select exit, customer can add more foods.
# calculate and display the bill at the end.
#sample menu
# # ==== Food Menu ===
# 1. Burger   Rs.1000
# 2.Pizza     Rs.1500

# -- Version 1 --
# foods = ["Burger", "Pizza", "Pasta" , "Rice"]
# prices = [800,1500,1000, 700]
#
# order_list = []
# total = 0
#
# while True : #infinite loop
#
#     # display menu
#     print("\n=== Food Menu ====")
#
#     for i in range(len(foods)):
#         print(f"{i+1}. {foods[i]:<10} - Rs.{prices[i]}")
#
#     print("Press '0' to Exit ")
#
#     choice = int(input("\nEnter Your  Choice : "))
#     #exit
#     if choice == 0 :
#         break
#
#     if 1 <= choice <= 4 :
#
#         item = foods[choice - 1]
#         price = prices[choice - 1]
#
#         order_list.append(item)
#         total += price
#
#         print(f"{item} added to your order .")
#
#     else :
#         print("Invalid Choice ! Please Try Again .")
#
#
# #display final order
# print("--- Your Order -----")
# for item in order_list :
#     print(item)
#
# print(f"{"":_<25}")
# print(f"Your total is : LKR {total}")

# ==========================
# VERSION 2.0

foods = ["Burger", "Pizza", "Pasta" , "Rice"]
prices = [800,1500,1000, 700]

order_items = []
total = 0

while True : #infinite loop

    # display menu
    print("\n=== Food Menu ====")

    for i in range(len(foods)):
        print(f"{i+1}. {foods[i]:<10} - LKR.{prices[i]}")

    print("Press '0' to Exit ")

    choice = int(input("\nEnter Your  Choice : "))
    #exit
    if choice == 0 :
        break

    if 1 <= choice <= 4 :
        item = foods[choice - 1 ]
        price = prices[choice - 1]

        #get quantity
        quantity = int(input(f"Enter Quantity of {item} : "))

        #calculate item total
        item_total = price * quantity

        order_items.append([item,price,quantity,item_total])

        #update total
        total += item_total

        print(f"{quantity} x {item} added to your order.")

    else :
        print("Invalid Input ! Try Again .")

#display final Bill

print("---------------------------")
print(f"{"Your Bill":^20}")
print("==========================")

# print(f"{'Item':<12}{'Price':<8}{'QTY':<6}{'Total':<12}")
print("Item       Price      QTY      Total")
print("--------------------------------------")

for order in order_items:
    item = order[0]
    price = order[1]
    qty = order[2]
    item_total = order[3]

    # print(f"{item}      {price}       {qty}   {item_total}")
    print(f"{item:<12}{price:>8}{qty:>6}{item_total:>12}")

print("------------------")
print(f"{'Total':<26} LKR.{total:>8}")
print("====================")
print("Thank You Come Again !")







