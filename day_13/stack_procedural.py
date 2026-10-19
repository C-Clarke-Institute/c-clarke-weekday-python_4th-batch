
book_stack = [] #stack is a last in first out data structure - LIFO

def push(elem):
    book_stack.append(elem)


def pop():
    if len(book_stack) > 1:
        popping_value = book_stack[-1]
        del book_stack[-1]
        return popping_value
    else:
        raise ValueError("List is empty")

try:
    push("Madol Duwa")
    push("GAGA Addara")
    popped_val = pop()
    print(popped_val)
    print(book_stack)
except ValueError as e:
    print(str(e))
