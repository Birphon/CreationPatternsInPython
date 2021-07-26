# factoryMethodDemo.py
"""  Purpose.  Factory Method  =            creation via inheritance   
Discussion.
 The architect has done an admirable job of decoupling the client
 from Stooge concrete derived classes, and, exercising polymorphism.
 But there remains coupling where instances are actually created.
 If we design an "extra level of indirection"
 (a "factory method")
 and have clients use it (instead of a hard coded constructor ),
 then the last bit of coupling goes away.
 The "factory method" (aka "virtual constructor") can be defined
 in the Stooge base class, or, in a separate "factory" class. """                              

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

class BetterMovie(object):
    def __init__(self):
        self.roles=[]
    def create(self):
        self.roles.append(Larry()) 
        self.roles.append(Moe()) 
        self.roles.append(Curley()) 
    def action(self):
        self.create()
        for role in self.roles:
            role.slapstick()
         
class NewMovie(BetterMovie):
    def create(self):
        self.roles.append(Moe()) 
        self.roles.append(Larry()) 
        self.roles.append(Curley()) 
    
if __name__== "__main__":
    print("\n\nCoupled version")
    m=Movie()
    m.action()
    print("\n\nDecoupled version")
    m=BetterMovie()
    m.action()
    print("\nAltered version")
    m=NewMovie()
    m.action()