
class A:

    def a_method(self):
        print("Calling from A class")

class B(A):

    def b_method(self):
        print("Calling from B method")

    def hello(self):
        print(f"Hello from B")

class C(A):
    def c_method(self):
        print("Calling from C method")

    def hello(self):
        print(f"Hello from C")

class D(B,C):

    def d_method(self):
        print("Calling from D method")


d = D()
d.hello()