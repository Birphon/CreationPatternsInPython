"""
!!!!!!!!REPLACE THIS LINE WITH YOUR NAME!!!!!!!!!!!!

This needs application of the PROTOTYPE pattern.
At present the client code at the bottom assembles many similar objects at run time.

Assume that the client needs to...
- turn out LOTS of identical objects
- does NOT usually want to have to worry about
  how an object is created, composed or represented
- occassionally also needs to produce a run of different(reconfigured) objects
"""

# do NOT change the PRODUCT classes below
class Graphic(object): # an ABSTRACT PRODUCT
    def __init__(self, scale):
        self.scale = scale
class Breve(Graphic): # a CONCRETE PRODUCT
    def __str__(self):
        return "a breve at " + self.scale
class Minim(Graphic):# a CONCRETE PRODUCT
     def __str__(self):
        return 'a minim at ' + self.scale
class Crotchet(Graphic):# a CONCRETE PRODUCT
    def __str__(self):
        return "a crotchet at " + self.scale
# CHANGE the class below class to give it PROTOTYPE functionality
class MusicScore(object):
    def __init__(self, title):
        self.title = title
        self.notes = []
    def addNote(self, newNote):
        self.notes.append( newNote )
    def __str__(self):
        me = self.title
        for note in self.notes:
            me += "\n\t" + str(note)
        me += '\n'
        return me
# the CLIENT code is below
# ASSUME THAT THIS CODE CAN *NOT* BE PUT IN AN __init__
# BUT *MUST* SOME HOW BE DONE AT RUNTIME
# note that the client is assembling objects 'at run time'
# and makes a lot of objects
# and that all the objects are basically the same
# SIMPLIFY THE CODE BELOW BY USING THE PROTOTYPE
basicScore1 = MusicScore('three blind mice')
basicScore1.addNote(Breve('b'))
basicScore1.addNote(Breve('a'))
basicScore1.addNote(Breve('g'))
print(basicScore1)

basicScore2 = MusicScore('three blind mice')
basicScore2.addNote(Breve('b'))
basicScore2.addNote(Breve('a'))
basicScore2.addNote(Breve('g'))
print(basicScore2)

basicScore3 = MusicScore('three blind mice')
basicScore3.addNote(Breve('b'))
basicScore3.addNote(Breve('a'))
basicScore3.addNote(Breve('g'))
print(basicScore3)

basicScore4 = MusicScore('three blind mice')
basicScore4.addNote(Breve('b'))
basicScore4.addNote(Breve('a'))
basicScore4.addNote(Breve('g'))
print(basicScore4)

basicScore5 = MusicScore('three blind mice')
basicScore5.addNote(Breve('b'))
basicScore5.addNote(Breve('a'))
basicScore5.addNote(Breve('g'))
print(basicScore5)

raceyScore1 = MusicScore('3 quick blind mice')
raceyScore1.addNote(Minim('b'))
raceyScore1.addNote(Minim('a'))
raceyScore1.addNote(Crotchet('g'))
print(raceyScore1)

raceyScore2 = MusicScore('3 quick blind mice')
raceyScore2.addNote(Minim('b'))
raceyScore2.addNote(Minim('a'))
raceyScore2.addNote(Crotchet('g'))
print(raceyScore2)
