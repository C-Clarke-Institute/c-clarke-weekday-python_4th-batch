

list1 = ["apple", 50, True , ["Colombo" , " Moratuwa", ], 5.0 ]

print(list1)
print(f"first element : {list1[0]}")
print(f"last element : {list1[-1]}")
print(f"third element : {list1[2]}")
# print(list1[-6])

list1.append("Orange")
print(list1)

# to find a index of element
print(list1.index(True))

shopping_list = ["apple", "biscuit" , "soap" , "water bottle"]


print("\n==== Shopping List ====")
for item in shopping_list:
    print(item)


print("\n-- using range --")
for i in range(len(shopping_list)):
    print(f"{i+1}. {shopping_list[i]}")