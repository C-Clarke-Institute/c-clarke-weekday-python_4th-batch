odd_numbers = 0
even_numbers = 0

user_input = int(input("Enter a number or -1 to exit "))

while user_input != -1:

    if user_input % 2 == 0 :
        even_numbers += 1 #even_numbers = even_numbers + 1
    else:
        odd_numbers += 1

    user_input = int(input("Enter a number or -1 to exit "))