import random

# students = ["Deneth", "Buddhika", "Nirmal", "Malith","Menura", "Gawrawa", "Minduli","Dilruk","Puleesha", "Vihanga"]
students = ["Gayan", "Minidu","Isuru","Chirath","Yumeera","Dilanga", "Rivipahan","Heshan","Deshan","Krishan", "Manujaya",
            "Malsha", "ileesha", "Isuru Dilshan", "Losan", "Bihara","Mayon","Jeewantha","Savindu", "Kavindu","Nemika","Isira","Vishwa",
            "Dinil", "Kavindu Navod", "Akaash", "Tharusha","Brayan", "Nithika", "Emalsha"]


random.shuffle(students)

print("Presentation Order \n----------")

with open("students_order_3rd_weekday.txt", "w") as file:

    number = 1

    for student in students:
        result = f"{number}. {student}"


        print(result)
        file.write(result + "\n")
        number += 1
