
student = {
    "name" : "supun",
    "age" : 20,
    "married" : True,
    "address" : "adadadad",
    "contact" : ["023232323", "234234234"],
    "parent_info" : {"name" : "iraj", "nic" : "232323233V"}
}

print(student["name"]) #Accessing values using a key in the dictionary

print(student["contact"][0])

student["contact"].append("232323235456")

for key in student.keys(): #Iterating over the keys
    print(f"Key - {key} | Value - {student[key]}")

for contact_no in student["contact"]:
    print(contact_no)

for val in student.values():#Iterating over the values
    print(val)

for key,val in student.items(): #Access both key and value
    print(f"key - {key} and val - {val}")

student["name"] = "Amal"
del student["age"] #Deleting a key value pair from a dictionary

student["grades"] = [30, 40, 50]

if "grades" in student.keys():
    print(student["grades"])

