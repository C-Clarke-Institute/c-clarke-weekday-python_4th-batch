

a = "test"
b = "2"
c = True

print(a,b)
print(a + b) # string concatenation
print(f"sghddg kjsd ksj {b}") # string formatting


# if (condition):
    #execution - if condition true run this
# else:
#     execution

# if a > 75 :
#     print( "A")
# else:
#     print("pass")
a = 78
if a > 75 :
    print("A")

if a > 65 :
    print("B")
if a > 55 :
    print("C"    )
else:
    print("W")



#loops

# 1 for loops
# 2 while loops

#for (var_name) in condition:
    #excution

for i in range(10): #0 - 10
    print("test" , i )

var = 0
print("-"*10)

while var < 50 : #while condition :
    print(var)
    var += 1

list1 = [1, 56, 78 , 89 , 45677 , 39978, 8970 , "strdgjh", 1.0, True ,[14, 67]]

tuple2 = 12 , 56, 76 , ()

print(list1)
print(f"1 index element of list1 - {list1[1]}")
# print("1 index element of list1 -" + list1[1])
list1[1] = "changed"
print(list1)
print(f"1 index element of list1 - {list1[1]}")

print(tuple2)
print(f"1 index element of tuple - {tuple2[1]}")

# tuple2[1] = "changed"
# print(list1)
# print(f"1 index element of tuple - {list1[1]}")
a = 5
b = 10



def add() : # function without arguments
    x = int(input("Enter Value 1 : "))
    y = int(input( "Enter Value 2 : "))

    print(x + y)


add()

def add_wit_args(x, y):
    print(x + y)

val1 = int(input("Enter Value 1 : "))
val2  = int(input( "Enter Value 2 : "))

add_wit_args(x=val2, y=val1) #keyword arguments
add_wit_args(val1,val2) #positianal arguments






