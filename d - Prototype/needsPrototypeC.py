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
class ProgramLine(object): # an ABSTRACT PRODUCT
    pass
class PrintLine(ProgramLine): # a CONCRETE PRODUCT
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "\tprint " + self.message
class InputLine(ProgramLine):# a CONCRETE PRODUCT
    def __init__(self, variable):
        self.variable = variable
    def __str__(self):
        return self.variable + ' = raw_input()' 
class IfLine(ProgramLine):# a CONCRETE PRODUCT
    def __init__(self, condition):
        self.condition = condition
    def __str__(self):
        return "if " + self.condition+ ":"
# CHANGE the class below class to give it PROTOTYPE functionality
class Program(object):
    def __init__(self, title):
        self.title = title
        self.lines = []
    def addLine(self, newLine):
        self.lines.append( newLine )
    def __str__(self):
        me = 'def ' + self.title + '():'
        for line in self.lines:
            me += "\n\t" + str(line)
        me += '\n'
        return me
# the CLIENT code is below
# ASSUME THAT THIS CODE CAN *NOT* BE PUT IN AN __init__
# BUT *MUST* SOME HOW BE DONE AT RUNTIME
# note that the client is assembling objects 'at run time'
# and makes a lot of objects
# and that all the objects are basically the same
# SIMPLIFY THE CODE BELOW BY USING THE PROTOTYPE
excitingGame1 = Program('guesMyNumber')
excitingGame1.addLine(InputLine('guess'))
excitingGame1.addLine(IfLine('guess != 42'))
excitingGame1.addLine(PrintLine('Nooooo!'))
print(excitingGame1)

excitingGame2 = Program('guesMyNumber')
excitingGame2.addLine(InputLine('guess'))
excitingGame2.addLine(IfLine('guess != 42'))
excitingGame2.addLine(PrintLine('Nooooo!'))
print(excitingGame2)

excitingGame3 = Program('guesMyNumber')
excitingGame3.addLine(InputLine('guess'))
excitingGame3.addLine(IfLine('guess != 42'))
excitingGame3.addLine(PrintLine('Nooooo!'))
print(excitingGame3)

excitingGame4 = Program('guesMyNumber')
excitingGame4.addLine(InputLine('guess'))
excitingGame4.addLine(IfLine('guess != 42'))
excitingGame4.addLine(PrintLine('Nooooo!'))
print(excitingGame4)

excitingGame5 = Program('guesMyNumber')
excitingGame5.addLine(InputLine('guess'))
excitingGame5.addLine(IfLine('guess != 42'))
excitingGame5.addLine(PrintLine('Nooooo!'))
print(excitingGame5)

xRatedGame1 = Program('xRatedGuessMyNumber')
xRatedGame1.addLine(InputLine('guess'))
xRatedGame1.addLine(IfLine('guess != 666'))
xRatedGame1.addLine(PrintLine('Nooooo!'))
print(xRatedGame1)

xRatedGame2 = Program('xRatedGuessMyNumber')
xRatedGame2.addLine(InputLine('guess'))
xRatedGame2.addLine(IfLine('guess != 666'))
xRatedGame2.addLine(PrintLine('Nooooo!'))
print(xRatedGame2)
