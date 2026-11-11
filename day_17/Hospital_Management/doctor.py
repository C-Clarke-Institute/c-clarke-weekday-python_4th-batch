

class Doctor :

    def __init__(self, name, doctor_id, consultation_fee, specilization):

        self.name = name
        self.doc_id = doctor_id
        self.special = specilization
        self.consultation_fee = consultation_fee

        # Print Doctor Data
    def display_info(self):
        print("----Doctor Data----")
        print(f"Name : {self.name}")
        print(f"Doctor Id: {self.doc_id}")
        print(f"Specialization: {self.special}")
        print(f"Cosultation Fee : {self.consultation_fee}")

    def update_specialization(self, new_special):
        self.special = new_special
        print("Doctor Specialization Updated Successfully")


