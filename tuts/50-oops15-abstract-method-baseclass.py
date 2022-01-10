from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def print_area(self):
        return 0

class Rectange(Shape):
    type = "Rectange"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        return self.length * self.breadth

rect1 = Rectange(5, 10)
print(rect1.print_area())
# obj1 = Shape()            # cannot create an object from abstract-class