class A():
    _instance = None
    def foo(self):
        return id(self)
    
def Singleton(Class):
    if not Class._instance:
        Class._instance = Class()
    return Class._instance

class B(A):
    pass
