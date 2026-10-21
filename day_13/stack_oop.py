class Stack:

    def __init__(self): #constructor
        self.stack_list = []

    def display(self):
        print(self.stack_list)

    def push(self, elem): #We call these methods, functions inside a class
        self.stack_list.append(elem)

    def pop(self):
        if len(self.stack_list) > 0:
            val = self.stack_list[-1]
            del self.stack_list[-1]
            return val
        else:
            raise ValueError("Stack is empty")


class CountingStack(Stack): #inheritance, is a relationship

    def __init__(self):
        Stack.__init__(self)
        self.__count = 0 #making count variable private

    def push(self, elem): #Method overriding
        Stack.push(self,elem)
        self.__count += 1

    def pop(self):
        self.__count -= 1
        return Stack.pop(self)

    def get_count(self):
        return self.__count

class AddingStack(Stack):
    
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def push(self, elem):
        self.__sum += elem
        super().push(elem)

    def pop(self):
        popped_val = super().pop()
        self.__sum -= popped_val
        return popped_val

    def get_sum(self):
        return self.__sum

    

counting_stack =  CountingStack() #creating an object from the class

counting_stack.push(20)
counting_stack.push(30)

counting_stack.count = 30

print("counting stack count - ", counting_stack.get_count())

book_stack = Stack()

book_stack.push("adadada")
book_stack.pop()
# game_stack = Stack()
# game_stack.push("GTA")

book_stack.display()
