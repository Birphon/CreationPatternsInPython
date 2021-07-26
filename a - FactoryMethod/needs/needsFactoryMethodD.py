"""
REPLACE THIS LINE WITH YOUR NAME

This needs application of the FACTORY METHOD pattern.
At present the ArtBook class assumes that a book
has a glossy firm cardboard cover and fine paper pages.

However the some new requirements for a new book have arisen
and reuse of the exitsting class is proving problematic.

The new requirements are for a different kind of Book
(a Teck Book )
with thin card covers and newsprint paper pages.
Notes:
Please also keep the 'old' kind of Book (ArtBook).
When you implement please use an ABSTRACT CREATOR class
(Book)
"""
# existing products
class Paper(object): # an ABSTRACT PRODUCT - keep it!
    def __str__(self):
        raise NotImplemented 
class Page(Paper):# a PRODUCT - keep it!
    def __str__(self):
        return "fine paper page"
class Cover(Paper):# a PRODUCT - keep it!
    def __str__(self):
        return "glossy firm cardboard cover"
#new products here

# Creators
class ArtBook(object): # an inflexible concrete CREATOR class
    def __init__(self, title): # MONOLITHIC method which does NOT 'abstract the instantiation process'
        # here is some creation 
        self.parts = []
        self.parts.append( Cover() )
        self.parts.append( Page() )
        self.parts.append( Page() )
        self.parts.append( Page() )
        self.parts.append( Page() )
        self.parts.append( Cover() )
        # the creation is mixed in with the following other 'essential stuff'
        self.title = title
        self.typeface = "Times New Roman"
        self.printingProcess = "4 colour offset printing"
    def __str__(self):
        me = "\nI am book about " + self.title  + " made up of..."
        for thing in self.parts:
            me += "\n" + str(thing)
        me +=  '\nI am printed in  ' + str(self.typeface)
        me +=  '\nand produced with ' + self.printingProcess
        return me
# the CLIENT code - which should know little about how things are constructed
artBook = ArtBook('Early Houses in Canterbury')
print(artBook)
"""
I am book about Early Houses in Canterbury made up of...
glossy firm cardboard cover
fine paper page
fine paper page
fine paper page
fine paper page
glossy firm cardboard cover
I am printed in  Times New Roman
and produced with 4 colour offset printing
"""
# the new requirements
# techBook = TechBook('GoF Patterns)
# print(techBook)
"""
I am book about GoF Patterns made up of...
thin card cover
newsprint paper page
newsprint paper page
newsprint paper page
newsprint paper page
thin card cover
I am printed in  Times New Roman
and produced with 4 colour offset printing
"""
