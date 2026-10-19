
x = "1233433x"

print(x.isdigit())
print(x.count("3"))
print(x.replace("3", "hello"))
print(x.isalpha())
print(x.isalnum())
print(x)

mail = "test@gmail.com"

if "@" in mail:
    print("yes")

print(mail.startswith("t"))
print(mail.endswith(".com"))