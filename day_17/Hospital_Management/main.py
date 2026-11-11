from day_17.Hospital_Management.doctor import Doctor
from day_17.Hospital_Management.patient import Patient

doctors = []
patients = []
appoinments = []

while 1:

    user_select = int(input("\n1. Create a Doctor"
                            "\n2. Create a Patient"
                            "\n3. Make a Appoinment"
                            ))


    if user_select == 1:

        doctor = Doctor("Dinal",1,5000,"special")
        doctors.append(doctor)

    if user_select == 2:
        patient = Patient("Test",25,'Male',"099898908989")
        patients.append(patient)

    if user_select == 3:
        pass
