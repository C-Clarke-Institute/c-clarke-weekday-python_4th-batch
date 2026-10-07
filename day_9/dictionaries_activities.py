employee = { "name" : "dinal",
             "age" : 28 ,
             "salary" : 50000.0 ,
             "department" : "IT"}


print(f"This employes's name is {employee['name']}. He is {employee['age']} old."
      f"He works in {employee['department']} department & earn {employee['salary']} in a month")

employee["name"] = "sanjula"
employee["Town"] = "colombo"

print(employee)

product = { "name" : "laptop", "price" : 180000, "stock" : 10}
# stock_status = "In stock " | "low stock" | "out of stock"
# if stock lower than 5 low stock

new_stock = int(input("Enter stock : "))
product['stock'] =  new_stock

print("Product : ", product['name'])
print("Price : ", product['price'])
print("Stock : ", product['stock'])

if product["stock"] == 0:
    print("Status : Out of stock")
elif product['stock'] <= 5 :
    print("Status : Low Stock")
else:
    print("Status : Product is available.")