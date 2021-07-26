"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the FACTORY METHOD pattern.
At present the LunchBox class assumes that a lunchbox
has a plastic ends and paper sides.

However the some new requirements for a new lunchbox have arisen
and reuse of the exitsting class is proving problematic.

The new requirements are for a different kind of Box
(a Sturdy Metal Box)
with metal sides and metal ends
Notes:
Please also keep the 'old' kind of Box (LunchBox).
When you implement please use an ABSTRACT CREATOR class
(Box)
"""
# existing products
class Wrapping(object): # an ABSTRACT PRODUCT - keep it!
    def __str__(self):
        raise NotImplemented 
class End(Wrapping):# a PRODUCT - keep it!
    def __str__(self):
        return "plastic end"
class Side(Wrapping):# a PRODUCT - keep it!
    def __str__(self):
        return "paper side"
#new products here

# Creators
class LunchBox(object): # an inflexible concrete CREATOR class
    def __init__(self, type): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( End() )
        self.parts.append( End() )
        self.parts.append( Side() )
        self.parts.append( Side() )
        self.parts.append( Side() )
        self.parts.append( Side() )
        # the creation is mixed in with the following other 'essential stuff'
        self.type = type
        self.colour = "Black"
        self.coating = "Wax"
    def __str__(self):
        me = "\nI am a " + self.type  + " made up of..."
        for thing in self.parts:
            me += "\n" + str(thing)
        me +=  '\ncoloured ' + str(self.colour)
        me +=  '\nand coated with ' + self.coating
        return me
# the CLIENT code - which should know little about how things are constructed
lunchBox = LunchBox('Classic Lunch Box')
print(lunchBox)
"""
I am a Classic Lunch Box made up of...
plastic end
plastic end
paper side
paper side
paper side
paper side
coloured Black
and coated with Wax
"""
# the new requirements
# sturdybox = metalBox('Sturdy Metal Box')
# print(sturdybox)
"""
I am a Sturdy Metal Box made up of...
metal end
metal end
metal side
metal side
metal side
metal side
coloured Black
and coated with Wax
"""
