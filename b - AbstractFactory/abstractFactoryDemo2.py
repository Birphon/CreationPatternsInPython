"""
Purpose.  Abstract Factory design pattern demo.

Discussion.  "Think of constructors as factories that churn out objects".
Here we are allocating the constructor responsibility to a factory object,
and then using inheritance and virtual member functions to provide a
"virtual constructor" capability.  So there are two dimensions of
decoupling occurring.  The client uses the factory object instead of "new"
to request instances; and, the client "hard-wires" the family, or class, of
that factory only once, and throughout the remainder of the application
only relies on the abstract base class.
"""


class Shape(object):
    total = 0
    def __init__(self):
        self.id = Shape.total
        Shape.total += 1
    def draw(self):
        return None

class Circle(Shape):
    def draw(self):
        print("circle ", self.id, ": draw")
        
class Square(Shape):
    def draw(self):
        print("square ", self.id, ": draw")
        
class Ellipse(Shape):
    def draw(self):
        print("ellipse ", self.id, ": draw")
        
class Rectangle(Shape):
    def draw(self):
        print("rectangle ", self.id, ": draw")

class Factory(object):
    def createCurvedInstance(self):
        pass
    def createStraightInstance(self):
        pass

class SimpleShapeFactory(Factory):
    def createCurvedInstance(self):
        return Circle()
    def createStraightInstance(self):
        return Square()

class RobustShapeFactory(Factory):
    def createCurvedInstance(self):
        return Ellipse()
    def createStraightInstance(self):
        return Rectangle()


if __name__ == "__main__":
    factory = SimpleShapeFactory()
    print("\nSimple")
    factory.createCurvedInstance().draw()
    factory.createStraightInstance().draw()
    factory.createCurvedInstance().draw()
    
    factory = RobustShapeFactory()
    print("\nRobust")
    factory.createCurvedInstance().draw()
    factory.createStraightInstance().draw()
    factory.createCurvedInstance().draw()

"""
circle  0 : draw
square  1 : draw
circle  2 : draw
ellipse  3 : draw
rectangle  4 : draw
ellipse  5 : draw
"""