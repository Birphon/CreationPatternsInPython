"""
Mike Lance

This needs application of the FACTORY METHOD pattern.
At present the Vehicle class assumes that a vehicle
has a Body and 4 wheels.

However the some new requirements for vehicle have arisen
and reuse of the exiting class is proving problematic.

The new requirements are for a different kind of vehicle
(MonsterTruck)
with a HugeBody and GiganticWheels
Notes:
Please also keep the 'old' kind of vehicle.
When you implement please use an ABSTRACT CREATOR class.
"""
class VehiclePart(object): # an ABSTRACT PRODUCT - keep it!
    pass 
class Body(VehiclePart):# a PRODUCT - keep it!
    def __str__(self):
        return "a Body"
class HugeBody(VehiclePart):# a new PRODUCT 
    def __str__(self):
        return "a HugeBody"
    
class Wheel(VehiclePart):# a PRODUCT - keep it!
    def __str__(self):
        return "a Wheel"

class GiaganticWheel(VehiclePart):# a new PRODUCT 
    def __str__(self):
        return "a GIGANTIC Wheel"
    
class Vehicle(object): # an ABSTRACT CREATOR class
    def makeBody(self):
        pass
    def makeWheel(self):
        pass
    def __init__(self): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( self.makeBody() )
        self.parts.append( self.makeWheel() )
        self.parts.append( self.makeWheel() )
        self.parts.append( self.makeWheel() )
        self.parts.append( self.makeWheel() )
        # the creation is mixed in with the following other 'essential stuff'
        self.origin = "NZ"
        self.quality = "hand crafted"
    def __str__(self):
        me = "\nI am made up of..."
        for thing in self.parts:
            me += "\n" + str(thing)
        me += "\nI am made in " + str(self.origin)
        me += "\nand my quality is " + self.quality
        return me

class Car(Vehicle):# a CONCRETE CREATOR class
    def makeBody(self):
        return Body()
    def makeWheel(self):
        return Wheel()

class MonsterTruck(Vehicle):# a CONCRETE CREATOR class
    def makeBody(self):
        return HugeBody()
    def makeWheel(self):
        return GiaganticWheel()    
# the CLIENT code - which should know little about how a car is constructed
car = Car()
print(car)
"""
I am made up of...
a Body
a Wheel
a Wheel
a Wheel
a Wheel
I am made in NZ
and my quality is hand crafted
"""
# the new requirements
biggie = MonsterTruck()
print(biggie)
"""
I am made up of...
a HUGE Body
a GIGANTIC Wheel
a GIGANTIC Wheel
a GIGANTIC Wheel
a GIGANTIC Wheel
I am made in NZ
and my quality is hand crafted
"""
