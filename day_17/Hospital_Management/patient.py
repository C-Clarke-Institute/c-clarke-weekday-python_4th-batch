
class Patient :

    def __init__(self, name , age , gender , contact_number):

        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact_number

    #Print Patient Data
    def display_info(self):

        print("----Patient Data----")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contact : {self.contact}")

    def update_contact(self, new_contact):

        self.contact = new_contact
        print("Contact Details Updated Successfully.")



