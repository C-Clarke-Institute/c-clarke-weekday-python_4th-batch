

two_dim_arr = [['x', 'x', 'x']
             , ['x', 'x', 'x'],
               ['x', 'x', 'x']]

print(len(two_dim_arr))


print(two_dim_arr[0])

two_dim_arr[0][0] = "Y"
print(two_dim_arr[0][0])


for element in two_dim_arr:
    print(element)
    for item in element:
        print(item)