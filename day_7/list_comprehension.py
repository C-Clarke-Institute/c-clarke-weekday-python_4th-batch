
numbers = []

for i in range(10):
    numbers.append(i)

nums = [i * 5 for i in range(10)]    #list comprehension

print(nums)

hello_list = ["hello" for i in range(10)]
print(hello_list)

even_numbers = [i for i in range(10) if i % 2 == 0]

print(even_numbers)