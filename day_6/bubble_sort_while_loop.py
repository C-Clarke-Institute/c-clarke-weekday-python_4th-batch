numbers = [9, 3, 4, 6, 7, 8, 10, 1, 5]

swapped = True

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)