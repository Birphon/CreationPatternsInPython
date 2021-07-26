""" Purpose.  Prototype                 
           creation via delegation
Discussion.  The architect has done an admirable job of decoupling the
client from Stooge concrete derived classes and exercising polymorphism.
But there remains coupling where instances are actually created.
If we design an "extra level of indirection" (a "factory") 
and have clients use it (instead of a constructor),
then the last bit of coupling goes away.
The Prototype pattern suggests delegating the creation service
to contained objects that know how to "clone" themselves.
This strategy also allows us to retire the "case" statement in "__main__"
"""

class Stooge(object):
    def slapStick(self):
        pass
    
class Larry(Stooge):
    def slapStick(self):
        print("Larry: poke eyes")

class Moe(Stooge):
    def slapStick(self):
        print("Moe: slap head")

class Curly(Stooge):
    def slapStick(self):
        print("Curly: suffer abuse")

if __name__ == "__main__":
    script = [ 0, 1, 2, 1 ]
    larry = Larry()
    moe = Moe()
    curly = Curly()
    for actor in script:
        if actor == 0:
            larry.slapStick()
        elif actor == 1:
            moe.slapStick()
        elif actor == 2:
            curly.slapStick()

"""
Larry: poke eyes
Moe: slap head
Curly: suffer abuse
Moe: slap head
"""