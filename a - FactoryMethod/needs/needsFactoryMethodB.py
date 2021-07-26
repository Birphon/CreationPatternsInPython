"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the FACTORY METHOD pattern.
At present the Buttie class assumes that a lunch
has a Baccon and tomatoe slices.

However the some new requirements for a new lunch have arisen
and reuse of the exitsting class is proving problematic.

The new requirements are for a different kind of snack
(a Pigout)
with cream and lots of chocolate
Notes:
Please also keep the 'old' kind of toy (Buttie).
When you implement please use an ABSTRACT CREATOR class
(Snack)
"""
# existing products
class Food(object): # an ABSTRACT PRODUCT - keep it!
    def __str__(self):
        raise NotImplemented 
class Tomatoe(Food):# a PRODUCT - keep it!
    def __str__(self):
        return "and a tomatoe slice"
class Baccon(Food):# a PRODUCT - keep it!
    def __str__(self):
        return "and bacon"
#new products here

# Creators
class Buttie(object): # an inflexible concrete CREATOR class
    def __init__(self, type): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( Baccon() )
        self.parts.append( Tomatoe() )
        self.parts.append( Tomatoe() )
        self.parts.append( Tomatoe() )
        self.parts.append( Tomatoe() )
        # the creation is mixed in with the following other 'essential stuff'
        self.type = type
        self.spread = "NZ butter"
        self.outer = "White Bread"
    def __str__(self):
        me = "\nI am a " + self.type  + " made up of...\n"
        me +=  str(self.outer)
        me +=  '\n' + self.spread
        for thing in self.parts:
            me += "\n" + str(thing)
        return me
# the CLIENT code - which should know little about how things are constructed
lunch = Buttie('Classic Tomatoe and Baccon Buttie')
print(lunch)
"""
I am a Classic Tomatoe and Baccon Buttie made up of...
White Bread
NZ butter
and bacon
and a tomatoe slice
and a tomatoe slice
and a tomatoe slice
and a tomatoe slice

"""
# the new requirements
# pigout = PigOut('Yummy Snack')
# print(pigout)
"""
I am a Yummy Snack made up of...
White Bread
NZ butter
and cream
and chocolate
and chocolate
and chocolate
and chocolate
"""
