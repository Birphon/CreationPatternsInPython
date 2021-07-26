""" Purpose.  Builder - NOT!
This monolithic design supports a single representation.
"""

class Array(object):
    def  __init__(self):
        self.lst = []
    def addFront(self, ch):
        self.lst.insert(0, ch)
    def addBack(self, ch):
        self.lst.append(ch)
    def traverse(self):
        print("\n",)
        for item in self.lst:
            print(item,)


if __name__ == "__main__":
    inputs = ("fa", "bb", "fc", "bd", "fe", "bf", "fg", "bh" )
    
    list = Array()

    for item in inputs:
        if item[0] == 'f':
            list.addFront( item[1] )
        elif item[0] == 'b':
            list.addBack( item[1] )
    list.traverse()

# g e c a b d f h
