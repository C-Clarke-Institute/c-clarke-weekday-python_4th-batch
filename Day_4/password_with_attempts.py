CORRECT_PASSWORD = "1234"
attempts = 3

while attempts > 0:
    password = input("\nEnter your Password : ")

    if password == CORRECT_PASSWORD:
        print("Login Successful")
        break

    else:
        print("\nWrong Password . Again ")
        attempts -= 1
        print(f"You have {attempts} attempts.")

if attempts == 0:
    print("\n🛑 YOUR ACCOUNT IS LOCKED.")
