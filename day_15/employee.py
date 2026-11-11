from dataclasses import dataclass


class Employee:
    def __init__(self, name_of_employee : str , position : str , salary : float):
        self.name = name_of_employee
        self.position = position
        self.base_salary = salary

    def calculate_salery(self):
        return  self.base_salary


class Manager(Employee):

    def __init__(self, name_of_employee: str, position: str, salary: float, bonus: float):
        super().__init__(name_of_employee,position,salary)
        self.bonus = bonus


    def calculate_salery(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, name_of_employee: str, position: str, salary: float, ot: float):
        super().__init__(name_of_employee, position, salary)
        self.overtime = ot

    def calculate_salery(self):
        return self.base_salary + self.overtime



dev1  = Developer("Dinal", "dev", 100000, 5000)

print(dev1.calculate_salery())








