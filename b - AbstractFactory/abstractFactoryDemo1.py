# abstractFactoryDemo1.py
"""
Abstract Factory classes are often implemented with Factory Methods,
but they can also be implemented using Prototype. [GOF, p95]
Abstract Factory might store a set of Prototypes
from which to clone and return product objects. [GOF, p126]
Factory Method: creation through inheritance.
Protoype: creation through delegation.
Virtual constructor: defer choice of object to create until run-time.
"""

class Expression(object):
    def __init__(self):
        self.text = ""
        self.list=[]
    def __str__(self):
        return self.text
    def clone(self):
        pass

class PCPhrase(Expression):
    next = 0;
    def __init__(self):
       Expression.__init__(self)
       self.list.append("animal companion\t")
       self.list.append("vertically challenged\t")
       self.list.append("factually inaccurate\t")
       self.list.append("chronologically gifted\t")
       self.text=self.list[PCPhrase.next]
       PCPhrase.next = (PCPhrase.next+1) % len(self.list)
    def clone(self):
       return PCPhrase()

class NotPCPhrase(Expression):
    next = 0
    def __init__(self):
        Expression.__init__(self)
        self.list.append("pet\t")
        self.list.append("short\t")
        self.list.append("lie\t")
        self.list.append("old\t")
        self.text = self.list[NotPCPhrase.next]
        NotPCPhrase.next = (NotPCPhrase.next+1) % len(self.list)
    def clone(self):
        return NotPCPhrase()


class Factory(object):
    def __init__(self):
        self.prototype = None
    def makePhrase(self):
        return self.prototype.clone()
    def makeCompromise(self):
        pass
    def makeGrade(self):
        pass

class PCFactory(Factory):
    def __init__(self):
        self.prototype = PCPhrase()
    def makeCompromise(self):
        expr = Expression()
        expr.text = "do it your way, any way, or no way"
        return expr
    def makeGrade(self):
        expr = Expression()
        expr.text = "you pass, self-esteem intact"
        return expr
    
class NotPCFactory(Factory):
   def __init__(self):
        self.prototype = NotPCPhrase()
   def makeCompromise(self):
        expr = Expression()
        expr.text = "my way, or the highway"
        return expr
   def makeGrade(self):
        expr = Expression()
        expr.text = "take test, deal with the results"
        return expr


if __name__ == "__main__":
    factory = PCFactory()
    print("\n**PC version**")
    for i in range(0,3):
        print(factory.makePhrase())
    print("\r")
    print(factory.makeCompromise())
    print(factory.makeGrade())

    factory = NotPCFactory()
    print("\n**NOT PC version**")
    for i in range(0,3):
        print(factory.makePhrase())
    print("\r")
    print(factory.makeCompromise())
    print(factory.makeGrade())

"""
**PC version**
vertically challenged	
factually inaccurate	
chronologically gifted	

do it your way, any way, or no way
you pass, self-esteem intact

**NOT PC version**
short	
lie	
old	

my way, or the highway
take test, deal with the results

"""