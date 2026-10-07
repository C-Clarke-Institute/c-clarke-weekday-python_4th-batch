password = "test@1996"
username = "test"

username_input = input("Enter your username")

if username == username_input: #True or False
    print("Congrats your username matches!")
    password_input = input("Enter your password : ")
    if password == password_input:
        print("Congrats your password matches as well!")
        print("""
        Welcome to our secret game
        1) press 1 to start the game
        """)
        user_input = input("Choice : ")
        if user_input == "1":
            print("Snake game is loading.......")
        else:
            print("Incorrect user input")
    else:
        print("Password is incorrect")
else:
    print("Entered username is incorrect")







print("zdfasdada")



