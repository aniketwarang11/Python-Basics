#from abc import ABCMeta , abstractmethod
from abc import ABC , abstractmethod #above 3.4
#class Shape(metaclass=ABCMeta) :
class Shape(ABC) : #above v3.4
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle (Shape) :
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length * self.breadth

rect = Rectangle()
print(rect.printarea())