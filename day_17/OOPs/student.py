from typing import List


class Student:

    student_count: int
    def __init__(self, student_id: str, name: str, age: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades: List[int] = []

    def __eq__(self, other) -> bool: #method overriding
        return self.student_id == other.student_id and self.name == other.name

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} | {self.student_id} | {self.age}"

std1 = Student(name="supun", student_id="001", age=20)
std2 = Student(name="supun", student_id="001", age=20)

print(std1)
if std1 == std2:
    print("Both students are equal")
else:
    print("Not equal")