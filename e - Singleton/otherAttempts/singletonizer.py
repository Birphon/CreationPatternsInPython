class Singletonizer(object):
    def __init__(self, baseClass):
        self.baseClass = baseClass
        self.obj = None       
    def __call__(self, *args, **kw):
        if self.obj is None:
            self.obj = apply(self.baseClass, args, kw)
        return self.obj
    
