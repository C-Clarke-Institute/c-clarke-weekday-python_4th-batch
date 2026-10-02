book_names = ["Science", "Maths", "history", "Religion"]

print(book_names[0])

book_names[3] = "Geography"

print(book_names[-1]) #Accessing the last element

print(book_names[-2]) #Access element before last element

for book_name in book_names:
    print(book_name)

print(len(book_names)) #Getting the length of a list

book_names.append("Atomic Habits")
print(book_names[-1])

book_names[0],book_names[-1] = book_names[-1], book_names[0]

book_names.insert(1, "SILO")

print(book_names)


del book_names[0]

print("After deleting", book_names)

if "Maths" in book_names:

    book_names.remove("Maths")

print(book_names[11])