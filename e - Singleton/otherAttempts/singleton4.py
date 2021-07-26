# Registry Singleton Ideas taken from Fredrik Lundh <Fredrik_Lundh@ivab.se>
#
# A Python Pattern: "Singleton/F"

class _SingletonRegistry(object):
    instance = None
    registry = {}
    def __init__(self):
        pass
    def getClass(self, Class, *args, **keywords):
        print "ARGS = " + str(args)
        print "class: " + str(Class)
        print "keywords: " + str(keywords)
        try:
            f = self.registry[Class]            
        except KeyError:
            self.registry[Class] = apply(Class, args, keywords)
        print "CLASS: " + str(self.registry[Class])
        return self.registry[Class]


def SingletonRegistry():
    """ Returns a SingletonRegistry reference, creating it if necessary """
    if not _SingletonRegistry.instance:
        _SingletonRegistry.instance = _SingletonRegistry()
    return _SingletonRegistry.instance


if __name__ == '__main__':
    class Foo(object):
        name = 'wee'

    class Bar(object):
        def __init__(self, *args):
            print "Bar.__init__ args: " + str(args)
            
    class Baz(object):
        def __init__(self, *args, **keywords):
            print "Bar.__init__ args: " + str(args)
            print "Baz.__init__ keywords: " + str(keywords)


    sr = SingletonRegistry()

    myFoo = sr.getClass(Foo)
    myFoo2 = sr.getClass(Foo)

    myBar = sr.getClass(Bar, "arg1", "arg2")
    myBar2 = sr.getClass(Bar, "arg1", "arg2")

    myBaz = sr.getClass(Baz, "arg1", "arg2", cheese=1, beer=2)
    myBaz2= sr.getClass(Baz, "arg1", "arg2", cheese=1, beer=2)

    print "myFoo  :" + str(myFoo)
    print "myFoo2 :" + str(myFoo2)
    print "myBar  :" + str(myBar)
    print "myBar2 :" + str(myBar2)
    print "myBaz  :" + str(myBaz)
    print "myBaz2 :" + str(myBaz2)
