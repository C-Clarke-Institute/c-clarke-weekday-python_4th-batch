
#Using read mode
file = open("test.txt", "r")
# content = file.read()
# print(content)
for line in file:
    print(line.strip())
file.close()

# print(file.readline())
# print(file.readline())
# print(file.readline())

file2 = open("student_info.txt", "w")
file2.write("amila,19,023343553\n")
file2.write("nisal,29,0334343553")
file2.close()

file3 = open("phone_no.txt", "a+") #read and write mode
file3.write("076232323\n")
file3.write("076252452\n")
file3.write("0837833677\n")
contacts = file3.read()
print(contacts)
file3.close()

with open("test.txt", "r") as f: #context manager
    for line in f:
        print(line.strip())

