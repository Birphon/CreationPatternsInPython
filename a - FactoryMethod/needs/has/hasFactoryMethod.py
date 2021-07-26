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

class ChallengingAttitude(Mind): # a PRODUCT - keep it!
    def __str__(self):
        return "Snips and snails"
class ChallengingTemperament(Mind):# a PRODUCT - keep it!
    def __str__(self):
        return "Puppy dogs tails!"
    
class Baby(object): # a CREATOR class(in the sense that creating a baby creates a mind)
    def makePersonality(self):
        return GoodAttitude()
    def makeAttitude(self):
        return GoodTemperament()
    def __init__(self): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.personality = []
        self.personality.append( self.makePersonality() )
        self.personality.append( self.makeAttitude() )
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
class ChallengingBaby(Baby):
    def makePersonality(self):
        return ChallengingAttitude()
    def makeAttitude(self):
        return ChallengingTemperament()    
# CLIENT CODE
girl = Baby()
print(girl)
boy = ChallengingBaby()
print(boy)