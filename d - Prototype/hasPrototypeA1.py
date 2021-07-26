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
class Prototype(object):
    def clone(self):
        import copy
        return copy.deepcopy(self)
# do NOT change the PRODUCT classes below
class BookPart(object): # an ABSTRACT PRODUCT
    pass
class Cover(BookPart): # a CONCRETE PRODUCT
    def __str__(self):
        return "a Cover"
class Page(BookPart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a page"
class GlossyGraphicPage(BookPart):# a CONCRETE PRODUCT
    def __str__(self):
        return "a GlossyGraphicPage"
# CHANGE the class below class to give it PROTOTYPE functionality
class Book(Prototype):
    def __init__(self, type):
        self.type = type
        self.parts = []
    def addPart(self, newPart):
        self.parts.append( newPart )
    def __str__(self):
        me = 'This ' + self.type + " is made up of..."
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
book1 = Book('Pocket Reference')
book1.addPart( Cover() )
book1.addPart( Page() )
book1.addPart( Page() )
book1.addPart( Page() )
book1.addPart( Page() )
book1.addPart( Cover() )
print(book1)

book2 = book1.clone()
print(book2)

book3 = book1.clone()
print(book3)

book4 = book1.clone()
print(book4)

book5 = book1.clone()
print(book5)


glossyBook1 = Book('Expensive Version')
glossyBook1.addPart( Cover() )
glossyBook1.addPart( Page() )
glossyBook1.addPart( Page() )
glossyBook1.addPart( GlossyGraphicPage() )
glossyBook1.addPart( Page() )
glossyBook1.addPart( Page() )
glossyBook1.addPart( Cover() )
print(glossyBook1)

glossyBook2 = glossyBook1.clone()
print(glossyBook2)
