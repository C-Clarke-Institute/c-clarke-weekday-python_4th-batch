#create a command line based quiz game
# the game randomly select questions from predefined questions bank
import random

# the player muse answer each  question correctly
# to procceed to the next question

# if player enter a incorrect answer he game ebd immedietly.

# the goal is to answer as many questions correctly as possible

questions = [
    {"question": "What is the capital of Sri Lanka?", "answer": "Sri Jayawardenepura Kotte"},
    {"question": "How many days are there in a week?", "answer": "7"},
    {"question": "What is 10 + 15?", "answer": "25"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "How many colors are there in a rainbow?", "answer": "7"},
    {"question": "What is the largest ocean in the world?", "answer": "Pacific Ocean"},
    {"question": "What is the chemical formula of water?", "answer": "H2O"},
    {"question": "Which animal is known as the King of the Jungle?", "answer": "Lion"},
    {"question": "How many months are there in a year?", "answer": "12"},
    {"question": "What is the opposite of hot?", "answer": "Cold"},
    {"question": "Which language is used to create web page structure?", "answer": "HTML"},
    {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"question": "What is 5 multiplied by 6?", "answer": "30"},
    {"question": "Which planet is closest to the Sun?", "answer": "Mercury"},
    {"question": "How many sides does a triangle have?", "answer": "3"},
    {"question": "Which country is famous for the Eiffel Tower?", "answer": "France"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "Which keyword is used to define a function in Python?", "answer": "def"},
    {"question": "What is the file extension for Python files?", "answer": ".py"},
    {"question": "Which data type stores True or False in Python?", "answer": "bool"}
]
question_number = 1
random.shuffle(questions)
print("=" * 40 )
print("Welcome to POP QUIZ")
print("=" * 40 )
for item in questions:
    print(f"\nQuestion {question_number} : ")
    print(item["question"])
    user_answer = input("Your Answer : ").strip()


    if user_answer.lower() == item["answer"].lower():
        print("Correct! Moving to the next question.")
        question_number += 1
    else:
        print("Wrong Answer! Game Over")
        break