class LazyHandle:
    def __init__(self, constructor, *args, **kwargs):
        self.__construct = (constructor, args, kwargs)
    def __call__(self):
        try:
            return self.__instance
        except AttributeError:
            self.__instance = apply(apply, self.__construct)
        return self.__instance


import time

class MySingleton:
    def __init__(self):
        self.created = time.time()


mysingleton = LazyHandle(MySingleton)

    # now we can just call mysingleton() to get the singleton
    print mysingleton().created   # lazily creates object

    time.sleep(3)

    print mysingleton().created   # prints the same time again


"""By placing such singletons in a central place, you can construct a
singleton registry. As a simple example:"""

class SingletonRegistry:
    pass

registry = SingletonRegistry()

registry.mysingleton = mysingleton

creation_time = registry.mysingleton().created


