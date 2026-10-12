
try:
    user_input = int(input("Enter a number : "))
    print(user_input + "test")
except ValueError as e: #handling an exception gracefully.
    print(f"Invalid user input - {str(e)}")
except TypeError: #Catching the most specific exception
    print("Type error occurred")
finally:
    print("finally block is executed")

try:
    user_input = int(input("Enter a number : "))
    print(user_input + "test")
except (ValueError,TypeError) as e: #handling multiple exceptions in a single catch block
    print("Error occurred")
finally:
    print("finally block is executed")


try:
    integer_input = int(input("Enter an Integer - : "))
    print(integer_input + "test")
except ValueError as e:
    print("Value error occurred")
except TypeError as e:
    print("Type error occurred")
except Exception as e:
    print(f"{str(e)}")

print("Hello world")