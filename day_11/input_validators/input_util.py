


def get_integer(prompt) :

    while True :
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Enter a valid number.")




def get_positive(prompt : int) :
    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                raise ValueError("Number Must be positive.")

            return number

        except ValueError as e :
            print("Invalid input :", e)
        except TypeError as e:
            print("Enter valid type ")

def get_menu_option(minimum, maximum):
    while True:
        choice = get_integer("Choose an option : ")

        if minimum <= choice <= maximum:
            return choice

        print(f"Choose a number from {minimum} to {maximum} : ")


print("1.menu number 1\n2.menu2\n3.Menu 3")
get_menu_option(1,3)




