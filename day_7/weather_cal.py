#write a code track the 3 temperature of a day to whole week
# must have a menu with 5 options
# 1 enter  the temperature
# 2. check temperature of specialise time
# 3. Average temp of a day
# 4. check the height temperature of a day
# 5. Average temp of week

#ask user for the days as input 1 to 7
#ask user for which hours as input 1 - 3
#ask user for the temp

#if user input date and time he can acess the temp
# if user enter a day, get average
# check highest temp of a day
#update the grid with the value
temps_per_day_for_week = [[0.0 for j in range(3)] for i in range(7)] #[0,1,2,3,4,5,6,7,8,9]

for temp in temps_per_day_for_week:
    print(temp)

average_temp = 0.0
hottest_day = 0

while 1:

    user_input = int(input("""\n
    1. Enter(update) the temperature
    2. To check temperature of specific time
    3. Average Temperature of a day
    4. Check highest Temperature of a day
    5. Average Temp of Week
    6. Exit 
    -----------------------
    \nEnter your menu option number : 
    """))

    if user_input == 1:
        day = int(input("Enter the day you want to input the data (1-7) : "))
        hour = int(input("Enter the time you want to input the data (1-3) : "))
        temp = int(input("Enter the temperature in celsius : "))

        temps_per_day_for_week [day-1][hour-1] = temp

        print("Temperature updated successfully..")

        for temp in temps_per_day_for_week:
            print(temp)


    elif user_input == 2:
        day = int(input("Enter the day you want to check the  temperature (1-7) : "))
        hour = int(input("Enter the time you want to check the data (1-3) : "))

        print(f"The temperature for {day} and {hour} is {temps_per_day_for_week [day-1] [hour-1]}")

    elif user_input == 3:
         day = int(input("Enter the day you want to check the average temperature (1-7) : "))

         total = 0

         for temp in temps_per_day_for_week[day] :
             total += temp

         average_temp = total / len(temps_per_day_for_week[day -1])

         print(f"The Average Temp of {day} is {average_temp} .")

    elif user_input == 4:
        day = int(input("Enter the day you want to check the highest temperature (1-7) : "))

        temperatures = temps_per_day_for_week[day - 1]
        hottest_temp = temperatures[0]

        for i in range(temperatures):
            if temperatures[i] > hottest_temp:
                hottest_temp = temperatures[i]
        print(f"Highest temperature of day {day} was {hottest_temp}")

    elif user_input == 5:
        total_temp = 0

        for day_temps in temps_per_day_for_week :
            for temp in day_temps :
                total_temp += temp

        print(f"Average Temperature of the week {total_temp/21}")

    elif user_input == 6:
        break

    else :
        print("Invalid Input ! try again . ")








