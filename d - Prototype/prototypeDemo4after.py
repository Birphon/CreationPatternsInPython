# not as good an implementation as prototypeDemo1a.py
# clone implementation is weak
# use of deepcopy better
class Stooge(object):
    def clone(self):
        pass
    def slapStick():
        pass

class Factory(object):
    def __init__(self):
        self.prototypes = []
    def get(self, num ):
        return self.prototypes[num]
    def add(self, prototype):
        self.prototypes.append(prototype)

class Larry(Stooge):
    def clone(self):
        return Larry()
    def slapStick(self):
        print("Larry: poke eyes")

class Moe(Stooge):
    def clone(self):
        return Moe()
    def slapStick(self):
        print("Moe: slap head")

class Curly(Stooge):
    def clone(self):
        return Curly()
    def slapStick(self):
        print("Curly: suffer abuse")


if __name__ == "__main__":
    script = [ 0, 1, 2, 1 ]
    factory = Factory()
    factory.add( Larry() )
    factory.add(  Moe() )
    factory.add(  Curly() )
    for actor in script:
        factory.get( actor).slapStick()

"""
Larry: poke eyes
Moe: slap head
Curly: suffer abuse
Moe: slap head
"""