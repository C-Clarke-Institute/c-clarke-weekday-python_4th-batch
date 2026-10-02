PASSWORD = "1234"

user_input = input("Enter Your Password : ")

while PASSWORD != user_input:
    print("\n❌ Wrong Password. Try Again")
    user_input = input("Enter Password : ")

print("Login Successfully ....")