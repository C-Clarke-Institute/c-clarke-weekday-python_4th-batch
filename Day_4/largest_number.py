#ask the user how many numbers they want to enter.
# collect  numbers and find the largest number among them

count = int(input("How many Numbers : "))

largest = int(input("Enter Your 1st Number : "))

for i in range (count-1):
    number = int(input(f"Enter Number {i+2} : "))

    if number > largest :
        largest = number

print(f"Largest Number : {largest}")