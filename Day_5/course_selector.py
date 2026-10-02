math = int(input("Enter Maths Marks : "))
science = int(input("Enter science Marks : "))
ICT = int(input("Enter ICT Marks : "))
english = int(input("Enter english Marks : "))

if math >= 60 and science >=60 and (ICT >= 60 or english >=  60 ):
    print("Admission Eligible")
else:
    print("Not Eligible")

