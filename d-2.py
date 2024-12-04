import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt((self.height**2) + (self.width**2))


rectangle1 = Rectangle(height=5, width=6)
print(format(rectangle1.area(), ".2f"))  # 30.00
print(format(rectangle1.diagonal(), ".2f"))  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(format(rectangle2.area(), ".2f"))  # 9.00
print(format(rectangle2.diagonal(), ".2f"))  # 4.24
