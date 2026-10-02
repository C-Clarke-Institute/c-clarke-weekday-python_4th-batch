user_input = float(input("Enter a Number :")) # type coversion used to convert str into integer
#because when every time we call input t return a string value.
# we cant do mathematical operations with strings


if user_input < 0 :
    print(f"{user_input} is a Negative Number")

elif user_input > 0 :
    print(f"{user_input} is a Positive Number")

else:
    print(f"{user_input} is a Zero")
