

def get_string(prompt : str):

    while True:

        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.Please try again.")

def get_integer(prompt : str):
    while True:
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print("Please enter a valid integer.")


def get_float(prompt: str):
    while True:
        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print("Please enter a valid floating number.")


def get_positive_numbers(prompt : str):

    while True:
        value = get_float(prompt)

        if value > 0 :
            return  value

        print("Value must be greater than zero.")



def get_yes_no(prompt : str):

    while True:

        value = input(prompt).strip().lower()

        if value in ("yes", "y"):
            return True

        if value in ("no", "n") :
            return False

        print("Pleade ENter Yea or no")







# name = get_string("Enter your name : ")