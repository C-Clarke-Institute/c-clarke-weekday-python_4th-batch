
#immutable
#mutable

nums = (12, 3, 4, 5) #Immutable
c,v,b,n = nums

print(c)
print(v)

# del nums[0]

nums2 = 3, 4, 5, 6, 7,8 #This is a tupel as well

#nums2.append(9)
print(nums2[1])
print(nums2)

def get_numbers():
    x = 10 #function scope
    y = 20

    return x, y

result = get_numbers()
print(result)


val1,val2 = result #Value unpacking
print(val1)


print("-----------")
def fun1(a, b, c):
    print(a + b + c)

fun1(5,10, 7)
fun1(a= 0, c= 45, b = 78)
fun1(6,c=10, b=6)

