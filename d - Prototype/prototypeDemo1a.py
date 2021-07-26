"""Purpose.  Prototype design pattern
1. Create a "contract" with clone() and .name entries
2. Design a "registry" that maintains a cache of prototypical objects
3. Populate the registry with an initializePrototypes() function
4. The registry has a findAndClone() "virtual constructor"
    that can transform a string into its correct object.
    It calls clone() which then calls deepcopy()
5. All classes relate themselves to the clone() contract
6. Client uses the findAndClone() virtual constructor
    instead of calling an actual constructor """

from copy import deepcopy
class Prototype(object):
    """ 1. The clone interface 
        Contract:  Each sub-class will copy itself FOR the client. """
    def __init__(self,name):
        self.name = name
    def clone(self):
        return deepcopy(self)

class PrototypesRegistry(object):
    """ 2. registry of prototypical objs """
    def __init__(self):
        self.prototypes = {}
    def addPrototype(self,obj):
        self.prototypes[obj.name] = obj
    def findAndClone(self, name ):
        """ 4. The virtual constructor """
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            print(name + " not found")
            return None

class Command(object):
    """  A contract interface """
    def execute(self):
        print(self.name + ": execute")

""" 5. Sign-up for the clone() """
class This(Prototype, Command): pass
class That(Prototype, Command): pass
class TheOther(Prototype, Command): pass

if __name__ == "__main__":
    data = ["Garbage", "This", "That", "Nothing", "TheOther"]
    objects = []
    p = PrototypesRegistry()
    """ 3. Populate the registry """
    p.addPrototype( This("This") )
    p.addPrototype( That("That") )
    p.addPrototype( TheOther("TheOther") )
    print("\n")
    for name in data:
        """ 6. Client does not create instances by calling constructors """
        o = p.findAndClone( name )
        if o != None:
            objects.append( o )
    for object in objects:
        object.execute()
"""
Garbage not found
Nothing not found
This: execute
That: execute
TheOther: execute
"""