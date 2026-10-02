age = int ( input("Enter your age : "))

if age >= 18:
    has_a_license = input("Do you have a license : (yes/no) ")

    if has_a_license == "yes":

        drunk = input("Are you drunk : (yes/no) : ")
        if drunk == "no":
            print("You are eligible to drive")
        else:
            print("You cant drive because of drunk ")
    else:
        print("Your are not eligible to drivee because you haven't a license")

else:
    print("Too young to drive")