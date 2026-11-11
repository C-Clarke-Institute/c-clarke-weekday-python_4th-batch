import datetime
from doctor import doc
from patient import  patient1
from day_17.Hospital_Management.doctor import Doctor
from day_17.Hospital_Management.patient import Patient


class Appointment :

    def __init__(self, appiint_number , doctor : Doctor, patient : Patient, date, time ):

        self.appointment_id = appiint_number
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def display_data(self):

        print(f"Appointment ID : {self.appointment_id}")
        print(f"Doctor_ID : {self.doctor.doc_id} - Name : {self.doctor.name}")
        print(f"Patient Name : {self.patient.name}")
        print(f"Appointment Date & Time : {self.date} | {self.time}")


