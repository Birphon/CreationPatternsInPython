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

car2 = Vehicle()
car2.type = "Car"
car2.addPart( Body() )
car2.addPart( Motor() )
car2.addPart( Wheel() )
car2.addPart( Wheel() )
car2.addPart( Wheel() )
car2.addPart( Wheel() )
print(car1)
print(car2)


car3 = Vehicle()
car3.type = "Car"
car3.addPart( Body() )
car3.addPart( Motor() )
car3.addPart( Wheel() )
car3.addPart( Wheel() )
car3.addPart( Wheel() )
car3.addPart( Wheel() )
print(car3)

car4 = Vehicle()
car4.type = "Car"
car4.addPart( Body() )
car4.addPart( Motor() )
car4.addPart( Wheel() )
car4.addPart( Wheel() )
car4.addPart( Wheel() )
car4.addPart( Wheel() )
print(car4)

car5 = Vehicle()
car5.type = "Car"
car5.addPart( Body() )
car5.addPart( Motor() )
car5.addPart( Wheel() )
car5.addPart( Wheel() )
car5.addPart( Wheel() )
car5.addPart( Wheel() )
print(car5)


# and also makes some motorcycles
motorcycle1 = Vehicle()
motorcycle1.type = 'Motorcycle'
motorcycle1.addPart( Body() )
motorcycle1.addPart( Motor() )
motorcycle1.addPart( Wheel() )
motorcycle1.addPart( Wheel() )
print(motorcycle1)

motorcycle2 = Vehicle()
motorcycle2.type = 'Motorcycle'
motorcycle2.addPart( Body() )
motorcycle2.addPart( Motor() )
motorcycle2.addPart( Wheel() )
motorcycle2.addPart( Wheel() )
print(motorcycle2)

# check that there are the objects: car1, car2, car3, car4, car5, motorcycle1, motorcycle2
print(dir())