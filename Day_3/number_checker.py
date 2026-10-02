num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 > num2:
    print(f"Number - {num1} is greater than number 2 - {num2}")
elif num2 > num1: #else if
    print(f"Number - 2 - {num2} is greater than number 1 - {num1}")
else:
    print("Both numbers are equal..........................")