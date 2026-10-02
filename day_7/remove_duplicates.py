
nums = [1, 4, 5, 6, 4, 4, 3, 2]

unique_nums = []

for num in nums:

    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)