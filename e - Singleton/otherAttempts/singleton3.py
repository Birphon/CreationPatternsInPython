class Singleton(object):
    __single = None
    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self

def Handle(x=Singleton):
    try:
        single = x()
    except Singleton, s:
        single = s
    return single

class Child(Singleton):
    def __init__(self, name):
        Singleton.__init__(self)
        self.__name = name
    def name(self):
        return self.__name

class Junior(Singleton):
    pass
        
