
user_input = input("Enter a word : ")

reversed_word = user_input[::-1]

if reversed_word == user_input:
    print(f"{user_input} is palindrome")