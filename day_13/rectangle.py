

class Rectangle:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_perimeter(self):

        return (self.__width + self.__height) * 2

    def calculate_area(self):
        return self.__height * self.__width

rect1 = Rectangle(10, 20)
print("rectangle1  perimeter- ", rect1.calculate_perimeter())

rect2 = Rectangle(20, 3)
print("rectangle2  perimeter- ", rect2.calculate_perimeter())
