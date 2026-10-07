contact_list = {"amal" : ["23232332", "23232321"]}#global scope
contact_list2 = {}
#add_contact
#search_contact
#remove_contact
#update_contact

def add_to_contact_list(phone_book, name, phone_no):
    if name not in phone_book:
        phone_book[name] = [phone_no] #{"saman" : ["232323332"]}
    else:
        if phone_no in phone_book[name]:
            print("Phone number already exists")
            return
        phone_book[name].append(phone_no) #{"saman" : ["23232323", "232332323"]}
def search_contact(phone_book, name):

    if name in phone_book.keys():
        print(f"Contact No of {name} - {phone_book[name]}")
    else:
        print("Contact not found")

def update_contact(phone_book, name, existing_no, new_no):

    if name in phone_book:
        contact_no_list = phone_book[name]
        if existing_no in contact_no_list:
            index = contact_no_list.index(existing_no)
            phone_book[name][index] = new_no
        else:
            print("Phone no not found in the list")
    else:
        print("User not found")

while True:

    choice = int(input("Enter your choice "
                   "\n Press 1 to add a contact"
                   "\n Press 2 to search contact"
                   "\n Press 3 to update contact"))

    if choice == 1:
        name_input = input("Enter your name : ")
        phone_no_input =  input("Enter your name : ")
        add_to_contact_list(phone_book=contact_list
                            , name=name_input, phone_no=phone_no_input)




