"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the PROTOTYPE pattern.
At present the client code at the bottom assembles a Computer at run time.

Assume that the client needs to...
- turn out LOTS of identical computers
- does NOT usually want to have to worry about how a computer  is created, composed or represented
- occassionally also needs to produce a run of different(reconfigured) computers
"""
from patterns import Prototype

class ComputerPart(object): # an ABSTRACT PRODUCT
    pass 
class Monitor(ComputerPart): # a CONCRETE PRODUCT
    def __str__(self):
        return "a Monitor"
class MotherBoard(ComputerPart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a MotherBoard"
class Keyboard(ComputerPart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a Keyboard"
#

class Computer(Prototype): 
    def __init__(self):
        self.parts = []
    def addPart(self, newPart):
        self.parts.append( newPart )
    def __str__(self):
        me = "\nA " + self.type + " made up of..."
        for part in self.parts:
            me += "\n\t" + str(part)
        return me
    
# the CLIENT code
# note that the client is assembling a Server 'at run time'
# and makes a lot of Servers
# and also makes some Desktop Systems


server1 = Computer()
server1.type = "Server"
server1.addPart( Monitor() )
server1.addPart( MotherBoard() )
server1.addPart( MotherBoard() )
server1.addPart( MotherBoard() )
server1.addPart( MotherBoard() )
server1.addPart( Keyboard() )
print( server1)

server2 = server1.clone()
print( server2)

desktop1 = Computer()
desktop1.type = 'Desktop'
desktop1.addPart( Monitor()  )
desktop1.addPart( MotherBoard() )
desktop1.addPart( Keyboard() )
print( desktop1)

server3 =  server1.clone()
print( server3)

desktop2  = desktop1.clone()
print( desktop2)
