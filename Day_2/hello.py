print("hello world", 123,"sdad", "dadasd") #passing multiple arguments to print function
print()
print("asdasd")

print(4.4)#float

print(3.)

print(True)
print(False)

print(6.66E-34)
print(1000)
print(1E3) #Exponent

print("hello", "world") #passsing positional arguments to a functions
print("hello", "world", sep="-") #passing keyword arguments with positional arguments
#keyword arguments must follow after positional arguments

# ====================================

#declare three string variables  , values of the variables should be city names
#print the cities in a single raw separated by comma using three methods
print("===================")
city1 = "Colombo"
city2 = "Moratuwa"
city3 = "Kandy"

print(city1,",",city2,",",city3)
print(city1,city3,city2,sep=",")
print(city1 + "," + city2 + " , " + city3) #concatinate
print(f"{city3},{city2},{city1}") # string formatting


print("-------------")
foods = "toffee"
stock = 10
# display this 2 variable in single line using concatenation
#print(foods + stock) this is wrong, we cant add string value and int values.
# to do that concatenation we use type conversion
print( foods + str(stock)) # this  called type conversion


