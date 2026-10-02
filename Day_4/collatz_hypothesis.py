
num = int(input("Enter a positive integer : "))

if num < 1:
    print("Please enter a valid positive integer")
    exit()

steps = 0

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1

    steps += 1

print(f"No of steps taken = {steps}")