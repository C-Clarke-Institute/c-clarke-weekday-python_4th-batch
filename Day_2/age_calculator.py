#Take current year as input
#Take birth year as input
#Calculate and output the age

current_year = int(input("Enter Current year - ")) #Type Conversion
birth_year = int(input("Enter birth year - "))

age = current_year - birth_year

print(f"User age is - {age} ")
print(type(current_year))