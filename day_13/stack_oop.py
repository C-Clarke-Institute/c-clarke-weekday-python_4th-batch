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

book_stack = Stack()

book_stack.push("adadada")
book_stack.pop()
# game_stack = Stack()
# game_stack.push("GTA")

book_stack.display()
