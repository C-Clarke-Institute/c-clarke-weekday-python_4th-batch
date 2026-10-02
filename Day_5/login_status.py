

#In python valid False values are - False, 0,0.0, "",None, [], {}, set(),()
is_logged_in = False
attempts = 0
max_attempts = 3

while not is_logged_in and attempts < max_attempts:

    print("\nPlease Login First.")

    username = input("enter your username : ")
    password = input("enter your password : ")

    if username == "admin" and password == "1234":
        is_logged_in = True
        print("Login Succesfull ! welcome admin")
    else:
        attempts += 1
        print("Invalid username or password")

        if attempts == max_attempts:
            print("Your Account is Locked. Please Contact Support.")



