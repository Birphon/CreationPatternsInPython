""" Purpose.  Prototype design pattern demo
Discussion. Image base class provides the mechanism for
storing, finding, and cloning the prototype for all derived classes.
Each derived class  "registers" a prototype of itself with the base class.
When the client asks for a "clone" of a certain type,
the base class is used to find the prototype and call clone() on the correct derived class.
"""

from copy import deepcopy

LSAT = 0 ; SPOT = 1

class Image(object):
    prototypes=[]
    def draw():
        pass
    def clone(self):
        return self.deepcopy()
    def returnType(self):
        pass

# NOT CLASSMETHODS
def findAndClone(imageType):
    """Client calls this function
        when it needs an instance of an Image subclass"""
    for prototype in Image.prototypes:
        if prototype.returnType() == imageType:
            return prototype.clone()
        else:
            print("Did not find Image Type")

def addPrototype( image):
    """As each subclass of Image is declared,
        it registers its prototype"""
    Image.prototypes.append(image)

class LandSatImage(Image):
    newID=0
    def __init__(self):
        self.id = LandSatImage.newID
        LandSatImage.newID += 1
    def clone(self):
        return LandSatImage()
    def returnType(self):
        return LSAT
    def draw(self):
        print("LandSatImage::draw " + str(self.id))

addPrototype(LandSatImage())

class SpotImage(Image):
    newID = 0
    def __init__(self):
        self.id = SpotImage.newID
        SpotImage.newID += 1
    def clone(self):
        return SpotImage()
    def returnType(self):
        return SPOT
    def draw(self):
        print("SpotImage::draw " + str( self.id ))


addPrototype(SpotImage())

if __name__ == "__main__":
    # Simulated stream of creation requests
    images = [ LSAT, LSAT, LSAT, SPOT, LSAT, SPOT, SPOT, LSAT ]
    print("\n")
    # Given an image type, find the right prototype, and return a clone
    for imageType in images:
        image = findAndClone( imageType )
        # Demonstrate that correct image objects have been cloned
        image.draw()

""" LandSatImage::draw 1
    LandSatImage::draw 2
    LandSatImage::draw 3
    SpotImage::draw 1
    LandSatImage::draw 4
    SpotImage::draw 2
    SpotImage::draw 3
    LandSatImage::draw 5 """