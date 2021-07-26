""" Purpose.  Builder
The monolithic design supports a single representation.
The Builder design allows a different representation
per Builder derived class,
and the common input and parsing have been defined in the Director class.
The Director constructs, the Builder returns the result.
"""

class Array(object):
    def __init__(self):
        self.lst = []
    def traverse(self):
        print("\n",)
        for item in self.lst:
            print(item,)

class Builder(object):
    def __init__(self):
        self.data = Array()
    def getResult(self):
        return self.data
    def addFront( self, char ):
        pass
    def addBack( self, char ):
        pass

class BuilderOne(Builder):
    def addFront( self, ch ):
        self.data.lst.append( ch )
    def addBack( self, ch ):
        self.data.lst.append( ch )

class BuilderTwo(Builder):
    def addFront( self, ch ):
        self.data.lst.insert(0, ch )
    def addBack( self, ch ):
        self.data.lst.append( ch )

class Director(object):
    def __init__(self, b):
        self.bldr = b
    def setBuilder(self, b):
        self.bldr = b
    def construct(self, inputs):
        for item in inputs:
            if item[0] == 'f':
                self.bldr.addFront(item[1])
            elif item[0] == 'b':
                self.bldr.addBack(item[1])


if __name__ == "__main__":
    input = ("fa", "bb", "fc", "bd", "fe", "bf", "fg", "bh" )

    one = BuilderOne()
    two = BuilderTwo()
    
    dir = Director(one)
    dir.construct(input)
    one.getResult().traverse()

    dir.setBuilder(two)
    dir.construct(input)
    two.getResult().traverse()

# a b c d e f g h
# g e c a b d f h