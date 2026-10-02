
#Declare empty list name it numbers.
#Store numbers from 0 - 10
#Then find the total of the numbers

numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)

total = 0

for num in numbers:
    total += num

print(sum(numbers))
