numbers  = [ -1, -2,-1.1 , -0.9 , 17,89,- 0.9, -4 ]

max_num = numbers[0]


for num in numbers:
    if num > max_num :
        max_num = num

print(f"Largest Number is  : {max_num}")

print("\n--- Even Numbers ----")
for num in numbers:
    if num % 2 == 0 :
        print(num)

for i in range(len(numbers)):
    if  numbers[i] % 2 == 0:
        print( numbers[i])

negative = []
positive = []

for num in numbers :

    if num >= 0 :
        positive.append(num)
    else:
        negative.append(num)

print("Negative Numbers ")
for num in negative :
    print(num)

print("\nPositive Numbers ")
for num in positive :
    print(num)


