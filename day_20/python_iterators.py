from typing import List

student_names: List[str] = ["amal", "nimal", "kamal", "sunimal"]

student_iterator = student_names.__iter__()

print(student_iterator)

try:
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
except StopIteration as e:
    print(e)

student_iterator2 = iter(student_names)
print(next(student_iterator2))

# for name in student_names:
#     print(name)

class CountDown: #Implementing iterator protocol

    def __init__(self, num: int):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num -= 1
        if self.num == 0:
            raise StopIteration

        return self.num

for i in CountDown(10): #Calls iterator method and then calls next method in each iteration
    print(i)

class NumberGenerator:

    def __init__(self, num: int):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.num:
            raise StopIteration
        return self.current

for i in NumberGenerator(100):
    print(i)

def generate_numbers(num):
    num_list =  []

    for i in range(num):
        num_list.append(i)

    return num_list

for j in generate_numbers(1000000000):
    print(j)