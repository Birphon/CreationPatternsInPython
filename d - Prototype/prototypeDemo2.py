# BUGS convertibf from C++
"""Purpose.  Prototype design pattern demo

Discussion.  Image base class provides the mechanism for storing,
 finding, and cloning the prototype for all derived classes.  Each
 derived class specifies a private static data member whose
 initialization "registers" a prototype of itself with the base class.
 When the client asks for a "clone" of a certain type, the base class
 finds the prototype and calls clone() on the correct derived class.
"""

LSAT=1
SPOT=2

class Image(object):
    prototypes=[]
    def draw(self):
        pass
    def findAndClone(self, imageType ):
        pass
    def returnType(self):
        pass
    def clone(self):
        pass
    def addPrototype( image ):
        prototypes.append( image )
        # As each subclass of Image is declared, it registers its prototype
    def findAndClone(self,  type ):
        for prototype in prototypes:
            if prototype.returnType() == type:
                return prototype.clone()
                #Client calls this public static member function
                #when it needs an instance of an Image subclass


class LandSatImage(Image):
    id = 0
    def __init__(self):
        # Nominal "state" per instance mechanism
        self.id = 0
        self.count = 0
    def returnType(self):
        return LSAT
    def draw(self):
        print("LandSatImage::draw " + self.id)
    #When clone() is called, call the one-argument ctor with a dummy arg
    def clone(self):
        return LandSatImage( 1 )
    # This is only called from clone()
    #LandSatImage( int dummy ) { _id = _count++; }
    #Mechanism for initializing an Image subclass - this causes the
    # default ctor to be called, which registers the subclass's prototype
    # static LandSatImage _landSatImage;
    # This is only called when the private static data member is inited
    # LandSatImage() { addPrototype( this ); }


# Register the subclass's prototype
#LandSatImage LandSatImage::_landSatImage;
# Initialize the "state" per instance mechanism
# int          LandSatImage::_count = 1;


class SpotImage(Image):
    count = 0
    def returnType(self):
        return SPOT
    def draw(self):
        print("SpotImage::draw " + self.id)
    def clone(self):
        return SpotImage( 1 )
    def __init__(self, num):
        self.id = SpotImage.count
        SpotImage.count += 1
        self.addPrototype( self )
        self.spotImage = None


# Simulated stream of creation requests
if __name__ == "__main__":
    image = Image()
    input = [ LSAT, LSAT, LSAT, SPOT, LSAT, SPOT, SPOT, LSAT ]
    # Given an image type, find the right prototype, and return a clone
    images=[]
    for anImage in input:
        images.append( image.findAndClone( image ) )
    # Demonstrate that correct image objects have been cloned
    for anImage in images:
        image.draw()
"""
LandSatImage::draw 1
LandSatImage::draw 2
LandSatImage::draw 3
SpotImage::draw 1
LandSatImage::draw 4
SpotImage::draw 2
SpotImage::draw 3
LandSatImage::draw 5
"""
