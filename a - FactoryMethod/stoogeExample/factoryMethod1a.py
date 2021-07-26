# factoryMethodDemo.py
"""
Purpose.
Factory Method  =            creation via inheritance

Discussion.
 The architect has done an admirable job of decoupling the client
 from Stooge concrete derived classes, and, exercising polymorphism.
 But there remains coupling where instances are actually created.

 If we design an "extra level of indirection"
 (a "factory method")
 and have clients use it (instead of a hard coded constructor ),
 then the last bit of coupling goes away.

 The "factory method" (aka "virtual constructor") can be defined
 in the Stooge base class, or, in a separate "factory" class.

THIS IS THE BEFORE VERSION WITH NO FACTORY METHODS

>>> m=Movie()
>>> m.action()
Larry: poke eyes
Moe: slap head
Curly: suffer abuse

"""

class Stooge(object):
    def slapstick(self):
        pass

class Larry(Stooge):
    def slapstick(self):
        print("Larry: poke eyes")
        
class Moe(Stooge):
    def slapstick(self):
     print("Moe: slap head")

class Curley(Stooge):
    def slapstick(self):
        print("Curly: suffer abuse")

class Movie(object):
    def __init__(self):
        self.roles=[]
        self.roles.append(Larry()) # coupling
        self.roles.append(Moe()) # coupling
        self.roles.append(Curley()) # coupling
    def action(self):
        for stooge in self.roles:
            stooge.slapstick()


def _test():
    import doctest, factoryMethod1a
    return doctest.testmod(factoryMethod1a, verbose=1)

if __name__ == "__main__":
    _test()