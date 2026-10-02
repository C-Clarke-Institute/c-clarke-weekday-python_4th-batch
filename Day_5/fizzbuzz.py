
#From numbers 0 - 20 if a number is divisible by 3 print Fizz,
# if a number is divisible by 5  print Buzz
#if a number is both divisible by 5 and 3 print fizzbuzz


for i in range(20):

    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")