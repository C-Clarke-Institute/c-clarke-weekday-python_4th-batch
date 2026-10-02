maths = int(input("Enter Maths Marks : "))
science = int(input("Enter Science Marks : "))
it = int(input("Enter IT marks : "))
english =  int(input("Enter English Marks :"))

total = maths + science + it + english
avg = total / 4
grade = 0

if avg >= 75 :
    grade = " A "
elif avg >= 65 :
    grade =  " B "
elif avg >= 55 :
    grade = " C"
elif avg >= 40:
    grade = " S"
else:
    grade = " W"

print("\n==================")
print(f"Your Total is {total}")
print(f"Your Average is {avg}")
print("*******************")
print(f"Your Final grade is {grade}")
print("\n==================")
