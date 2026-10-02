#write a program to check if a number is dividable by 5,
# if its dividable by 5 print true

user_input = int(input("Enter Your Number : "))

print(f"does {user_input} dividable by 5 : {(user_input % 5) == 0}")
