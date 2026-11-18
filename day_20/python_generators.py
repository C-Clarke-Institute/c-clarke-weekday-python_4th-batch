
def num_generator():
    yield 10
    yield 22
    yield 33
    yield 22

gen = num_generator()

for i in num_generator():
    print(i)