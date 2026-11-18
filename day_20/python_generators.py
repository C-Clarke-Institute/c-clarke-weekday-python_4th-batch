import platform

print(platform.system())

def num_generator():
    yield 10
    yield 22
    yield 33
    yield 22

def generate_numbers(num):
    for i in range(num):
        yield i


even_num_list = [i for i in range(10) if i % 2 == 0] #List comprehension
even_num_gen = (i for i in range(10) if i % 2 == 0) #Generator expression

print("Even number list", even_num_list)
print("Even number generator", even_num_gen)



gen = num_generator()
# for i in generate_numbers(100):
#     print(i)
#
#
# for i in num_generator():
#     print(i)