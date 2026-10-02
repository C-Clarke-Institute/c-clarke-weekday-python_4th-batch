
first_num = int(input("Enter first num : "))
second_num = int(input("Enter Second num : "))
operator = input("Enter operator : ")

if operator == "+":
    print(f"Result : {first_num + second_num}")
elif operator == "-":
    print(f"Result : {first_num - second_num}")
elif operator == "*":
    print(f"Result : {first_num * second_num}")
elif operator == "/":
    if second_num == 0:
        print("Cannot be divided by zero")
    else:
        print(f"Result : {first_num / second_num}")