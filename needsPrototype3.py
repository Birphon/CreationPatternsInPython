"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the PROTOTYPE pattern.
At present the client code at the bottom assembles a RoundOfDrinks at run time.

Assume that the client needs to...
- turn out LOTS of orders of drinks for Trev
- does NOT usually want to have to worry about how the drinks are created, composed or represented
- occasionally also needs to produce a order of different(reconfigured) drinks for Mike
"""
class Drink(object): # an ABSTRACT PRODUCT
    pass 
class Speights(Drink): # a CONCRETE PRODUCT
    def __str__(self):
        return "Speights"
class Whiskey(Drink):# a CONCRETE PRODUCT
    def __str__(self):
        return "Wiskey"
class Water(Drink):# a CONCRETE PRODUCT
    def __str__(self):
        return "Water"
#
class RoundOfDrinks(object): 
    def __init__(self):
        self.drinks = []
    def addDrink(self, newDrink):
        self.drinks.append( newDrink )
    def __str__(self):
        me = "\n" + self.orderer + " here is your order of "
        for drink in self.drinks:
            me += "\n\t" + str( drink )
        return me
    
# the CLIENT code
# note that the client is assembling a drinks order 'at run time'
# and makes a lot of Trev Drinks
# and also makes some  drinks for others


TrevOrder1 = RoundOfDrinks()
TrevOrder1.orderer = "Trev"
TrevOrder1.addDrink( Speights() )
TrevOrder1.addDrink( Speights() )
TrevOrder1.addDrink( Speights() )
TrevOrder1.addDrink( Speights() )
TrevOrder1.addDrink( Speights() )
TrevOrder1.addDrink( Speights() )
print( TrevOrder1 )

TrevOrder2 = RoundOfDrinks()
TrevOrder2.orderer = "Trev"
TrevOrder2.addDrink( Speights() )
TrevOrder2.addDrink( Speights() )
TrevOrder2.addDrink( Speights() )
TrevOrder2.addDrink( Speights() )
TrevOrder2.addDrink( Speights() )
TrevOrder2.addDrink( Speights() )
print( TrevOrder2 )

MikeOrder1 = RoundOfDrinks()
MikeOrder1.orderer = "Mike"
MikeOrder1.addDrink( Whiskey() )
MikeOrder1.addDrink( Water() )
print( MikeOrder1 )

TrevOrder3 = RoundOfDrinks()
TrevOrder3.orderer = "Trev"
TrevOrder3.addDrink( Speights() )
TrevOrder3.addDrink( Speights() )
TrevOrder3.addDrink( Speights() )
TrevOrder3.addDrink( Speights() )
TrevOrder3.addDrink( Speights() )
TrevOrder3.addDrink( Speights() )
print( TrevOrder3 )

MikeOrder2 = RoundOfDrinks()
MikeOrder2.orderer = "Mike"
MikeOrder2.addDrink( Whiskey() )
MikeOrder2.addDrink( Water() )
print( MikeOrder2 )