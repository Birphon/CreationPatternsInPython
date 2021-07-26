"""
!!!!!!!!REPLACE THIS LINE WITH YOUR NAME!!!!!!!!!!!!

This needs application of the PROTOTYPE pattern.
At present the client code at the bottom assembles a Car at run time.

Assume that the client needs to...
- turn out LOTS of identical cars
- does NOT usually want to have to worry about
  how a car is created, composed or represented
- occassionally also needs to produce a run of different(reconfigured) vehicles
"""
class VehiclePart(object): # an ABSTRACT PRODUCT
    pass
class Motor(VehiclePart): # a CONCRETE PRODUCT
    def __str__(self):
        return "a Motor"
class Body(VehiclePart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a Body"
class Wheel(VehiclePart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a Wheel"
#
from copy import deepcopy
class Vehicle(object):
    def __init__(self):
        self.parts = []
    def addPart(self, newPart):
        self.parts.append( newPart )
    def __str__(self):
        me = 'This ' + self.type + " is made up of..."
        for part in self.parts:
            me += "\n\t" + str(part)
        return me
    def clone(self):
        return deepcopy(self)
# the CLIENT code
# ASSUME THAT THIS CODE CAN *NOT* BE PUT IN AN __init__
# BUT *MUST* SOME HOW BE DONE AT RUNTIME
# note that the client is assembling a car 'at run time'
# and makes a lot of cars
# and all Cars are basically the same
car1 = Vehicle()
car1.type = "Car"
car1.addPart( Body() )
car1.addPart( Motor() )
car1.addPart( Wheel() )
car1.addPart( Wheel() )
car1.addPart( Wheel() )
car1.addPart( Wheel() )
print(car1)

car2 = car1.clone()
print(car2)

car3 =  car1.clone()
print(car3)

car4 = car1.clone()
print(car4)

car5 =  car1.clone()
print(car5)


# and also makes some motorcycles
motorcycle1 = Vehicle()
motorcycle1.type = 'Motorcycle'
motorcycle1.addPart( Body() )
motorcycle1.addPart( Motor() )
motorcycle1.addPart( Wheel() )
motorcycle1.addPart( Wheel() )
print(motorcycle1)

motorcycle2 = motorcycle1.clone()
print(motorcycle2)

# check that there are the objects: car1, car2, car3, car4, car5, motorcycle1, motorcycle2
print(dir())