from dataclasses import dataclass, field
from typing import List, ClassVar


@dataclass
class Student:

    student_count : ClassVar[int] = 0 #Defining a class variable in dataclass

    __name:str #encapsulating name instance variable
    age: int
    student_id: str
    grades: List[int] = field(default_factory=list)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    def get_name(self):
        return self.__name

std1 = Student("amal", age=20, student_id="001")
std2 = Student("amal", age=20, student_id="001")
print(Student.student_count)
print(std1)

if std1 == std2:
    print("Both are equal")