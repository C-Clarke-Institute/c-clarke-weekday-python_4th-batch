
def hello():
    print("Hello")
    return hello()


# hello()

def countdown(n):
    print(n)
    if n == 0:
        return
    return countdown(n-1)


def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def sum_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return sum_fib(n -1) + sum_fib(n - 2)

result = sum(3)
val1 = sum_fib(6)
print(val1)
print(result)
countdown(5)


numbers = [10, 4,54, 5677, 999]


def find_largest(numbers, n) :

    #base case
    if n == 1 :
        return numbers[0]

    #recursive call
    largest = find_largest(numbers, n - 1)

    if numbers[n - 1] > largest:
        return numbers[n-1]

    return largest



result = find_largest(numbers, len(numbers))


print("Largest : ", result)


def reverse_numbers(num, reversed_num = 0):

    # base case
    if num == 0:
        return reversed_num

    #get the last digit
    last_digit = num % 10

    reversed_num = reversed_num * 10 + last_digit

    return reverse_numbers(num // 10, reversed_num)









