# get avarge score from 4 subjects

# to qualified for scolarsip he must have average above 75, attandance above 75 and
# income less than 10000 or special achivements

# if he elgible for the scalarship base on his aaveragee he got scolarship
# avarge above 90 got 100% scolarship
# above 80 got 75%
# others 50%


math = int(input("Enter Maths Marks : "))
science = int(input("Enter science Marks : "))
ICT = int(input("Enter ICT Marks : "))
english = int(input("Enter english Marks : "))

avg = (math + science + ICT + english)/4
attendance = float(input("Please Enter Your Attendance ( 0 - 100 % ): "))
monthly_income = float(input("Please Enter Your Income : "))
is_achivements = input("do you have special achivements : ") == "yes"

if avg  >= 75 and attendance >= 75 and ( monthly_income <= 100000 or is_achivements):

    if avg >=  90 :
        print(" You are eligible for 100% Scholarship")

    elif avg >=  80 :
        print(" You are eligible for 75% Scholarship")

    else:
        print(" You are eligible for 50% Scholarship")

else:
    print("You are not eligible for scholarship")




