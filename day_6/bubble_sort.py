numbers = [9, 3, 4, 6, 7, 8, 10, 1, 5]

for j in range(len(numbers)): #Big O notation  -
    for i in range(len(numbers) - 1 - j):

        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i + 1], numbers[i]

print(numbers)        

