"""
This needs application of the FACTORY METHOD pattern.
At present the Baby class assumes that a baby
has a GoodAttitude and a GoodTemperament.

However the some new requirements for Baby have arisen
and reuse of the exitsting class is proving problematic.

The new requirements are for a different kind of baby with
a ChallengingAttitude ("Snips & Snails")
and a ChallengingTemperament ("Puppy dogs tails!")

Note: please keep the 'old' kind of Baby!!
"""
class Mind(object): # an ABSTRACT PRODUCT - keep it!
    pass 
class GoodAttitude(Mind): # a PRODUCT - keep it!
    def __str__(self):
        return "Sugar & Spice."
class GoodTemperament(Mind):# a PRODUCT - keep it!
    def __str__(self):
        return "All things nice!"
    
class BadAttitude(Mind): # a PRODUCT - keep it!
    def __str__(self):
        return "Snips & Snails."
class BadTemperament(Mind):# a PRODUCT - keep it!
    def __str__(self):
        return "Puppy dogs tails!"
    
class Baby(object): # a CREATOR class(in the sense that creating a baby creates a mind)
    def makeAttitude(self):
        pass
    def makeTemperament(self):
        pass
    
    def __init__(self): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.personality = []
        self.personality.append( self.makeAttitude() )
        self.personality.append( self.makeTemperament() )
        # the creation above is mixed in with the following other 'essential stuff' below
        self.age = 0
        self.value = "treasured!"
    def __str__(self):
        me = "\nI am made up of..."
        for thing in self.personality:
            me += "\n" + str(thing)
        me += "\nMy age is " + str(self.age)
        me += "\nI am " + self.value
        return me

    
class GoodBaby(Baby): # a CREATOR class(in the sense that creating a baby creates a mind)
    def makeAttitude(self):
        return GoodAttitude()
    def makeTemperament(self):
        return GoodTemperament()
    
    
class BadBaby(Baby): # a CREATOR class(in the sense that creating a baby creates a mind)
    def makeAttitude(self):
        return BadAttitude()
    def makeTemperament(self):
        return BadTemperament()
   


# CLIENT CODE
girl = GoodBaby()
print(girl)
boy = BadBaby()
print(boy)






