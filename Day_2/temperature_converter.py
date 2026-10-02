#create a simple CLI base Temperature converter
# ask the  user to enter current temperature in Celsius
# convert them in to kelvin and Fahrenheit
#0 celsius is 273.15 kelvin | [Celsius to Fahrenheit Formula ( 1C x 9/5) + 32]


current_temp = float(input("Enter Temperature in Celsius : "))

kelvin_temp = current_temp + 273.15
fahrenheit_temp = (current_temp * 9 / 5) + 32

print( f"{current_temp} in Celsius equal to \n{kelvin_temp} "
       f"in Kelvin & \n{fahrenheit_temp} in Fahrenheit")