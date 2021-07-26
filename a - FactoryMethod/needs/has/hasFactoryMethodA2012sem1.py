"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the FACTORY METHOD pattern.
At present the TeddyBear class assumes that a toy
has a Body and 4 limbs.

However the some new requirements for a new toy have arisen
and reuse of the exitsting class is proving problematic.

The new requirements are for a different kind of toy
(Python)
with a LongBody and 4 black stripes
Notes:
Please also keep the 'old' kind of toy (TeddyBear.
When you implement please use an ABSTRACT CREATOR class
(Toy)
"""
# existing products
class ToyPart(object): # an ABSTRACT PRODUCT - keep it!
    def __str__(self):
        raise NotImplemented 
class Body(ToyPart):# a PRODUCT - keep it!
    def __str__(self):
        return "a Body"
class Limb(ToyPart):# a PRODUCT - keep it!
    def __str__(self):
        return "and a limb"
#new products here
class LongBody(ToyPart):# a new PRODUCT - need to do this!
    def __str__(self):
        return "a LONG Body"
class Stripe(ToyPart):# a PRODUCT - keep it!
    def __str__(self):
        return "and a black stripe"

# Creators
class TeddyBear(object):
    def makeBody(self):
        return Body()
    def makeBodyExtra(self):
        return Limb()
    
    def __init__(self, type): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( self.makeBody() )
        self.parts.append( self.makeBodyExtra()  )
        self.parts.append( self.makeBodyExtra() )
        self.parts.append( self.makeBodyExtra() )
        self.parts.append( self.makeBodyExtra() )
        # the creation is mixed in with the following other 'essential stuff'
        self.type = type
        self.origin = "NZ"
        self.quality = "hand crafted"
        
    def __str__(self):
        me = "\nI am a " + self.type  + " made up of..."
        for thing in self.parts:
            me += "\n" + str(thing)
        me += "\nI am made in " + str(self.origin)
        me += "\nand my quality is " + self.quality
        return me   
class Python(TeddyBear):
    def makeBody(self):
        return LongBody()
    def makeBodyExtra(self):
        return Stripe()
    
    '''
    def __init__(self, type): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( LongBody() )
        self.parts.append( Stripe() )
        self.parts.append( Stripe() )
        self.parts.append( Stripe() )
        self.parts.append( Stripe() )
        # the creation is mixed in with the following other 'essential stuff'
        self.type = type
        self.origin = "NZ"
        self.quality = "hand crafted"
    '''
# the CLIENT code - which should know little about how construct happens
ted = TeddyBear('Classic Teddy Bear')
print(ted)
"""
I am a Classic Teddy Bear made up of...
a Body
a limb
a limb
a limb
a limb
I am made in NZ
and my quality is hand crafted
"""
# the new requirements
snake = Python('African Rock Python')
print(snake)
"""
I am a African Rock Python made up of...
a LONG Body
and a black stripe
and a black stripe
and a black stripe
and a black stripe
I am made in NZ
and my quality is hand crafted
"""
