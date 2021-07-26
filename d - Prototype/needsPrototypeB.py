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
class WindowControl(object): # an ABSTRACT PRODUCT
    pass
class Frame(WindowControl): # a CONCRETE PRODUCT
    def __str__(self):
        return "a Frame"
class InputBox(WindowControl):# a CONCRETE PRODUCT
    def __str__(self):
        return "an Input Box"
class Button(WindowControl):# a CONCRETE PRODUCT
    def __init__(self, label):
        self.label = label
    def __str__(self):
        return "a Button saying '" + self.label + "'"
# CHANGE the class below class to give it PROTOTYPE functionality
class WindowDialog(object):
    def __init__(self, title):
        self.title = title
        self.parts = []
    def addPart(self, newPart):
        self.parts.append( newPart )
    def __str__(self):
        me = 'This dialog is called "' + self.title + '" and has ...'
        for part in self.parts:
            me += "\n\t" + str(part)
        return me
# the CLIENT code is below
# ASSUME THAT THIS CODE CAN *NOT* BE PUT IN AN __init__
# BUT *MUST* SOME HOW BE DONE AT RUNTIME
# note that the client is assembling objects 'at run time'
# and makes a lot of objects
# and that all the objects are basically the same
# SIMPLIFY THE CODE BELOW BY USING THE PROTOTYPE
dialog1 = WindowDialog('Format your hard drive now?')
dialog1.addPart( Button('OK') )
dialog1.addPart( Button('Maybe') )
dialog1.addPart( Button('Nooooo!') )
print(dialog1)

dialog2 = WindowDialog('Format your hard drive now?')
dialog2.addPart( Button('OK') )
dialog2.addPart( Button('Maybe') )
dialog2.addPart( Button('Nooooo!') )
print(dialog2)

dialog3 = WindowDialog('Format your hard drive now?')
dialog3.addPart( Button('OK') )
dialog3.addPart( Button('Maybe') )
dialog3.addPart( Button('Nooooo!') )
print(dialog3)

dialog4 = WindowDialog('Format your hard drive now?')
dialog4.addPart( Button('OK') )
dialog4.addPart( Button('Maybe') )
dialog4.addPart( Button('Nooooo!') )
print(dialog4)

dialog5 = WindowDialog('Format your hard drive now?')
dialog5.addPart( Button('OK') )
dialog5.addPart( Button('Maybe') )
dialog5.addPart( Button('Nooooo!') )
print(dialog5)


kindDialog1 = WindowDialog('Format whose hard drive now?')
kindDialog1.addPart( InputBox() )
kindDialog1.addPart( Button('Do It!') )
kindDialog1.addPart( Button('Maybe NOT!') )
kindDialog1.addPart( Button('Just pick somebody at random please') )
print(kindDialog1)

kindDialog2 = WindowDialog('Format whose hard drive now?')
kindDialog2.addPart( InputBox() )
kindDialog2.addPart( Button('Do It!') )
kindDialog2.addPart( Button('Maybe NOT!') )
kindDialog2.addPart( Button('Just pick somebody at random please') )
print(kindDialog2)
