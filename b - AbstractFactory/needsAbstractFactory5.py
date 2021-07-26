"""
REPLACE THIS LINE WITH YOUR NAME
"""
# There are two families of related products
# AbstractProductA
class PythonSyntax(object):
    def get():
        return None
# ConcreteProductA1
class StartPythonPrint(PythonSyntax):
    def get(self):
        return "print( '"
# ConcreteProductA2
class EndPythonPrint(PythonSyntax):
    def get(self):
        return ")'"
#AbstractProductB
class JadeSyntax(object):
    def get():
        return None
# ConcreteProductB1
class StartJadeWrite(JadeSyntax):
    def get(self):
        return 'write "'
# ConcreteProductB2
class EndJadeWrite(JadeSyntax):
    def get(self):
        return '";'

"""
The CLIENT code below currently has to make too many decisions
and know all about the food choices

Change things by applying the ABSTRACT FACTORY pattern
so the client only has to decide the type of feast
and does not need to know the details of feast preparation.

To make things simplier can you please ..
get rid of the constants (too much to remember)
get rid of the case statements (too difficult to maintain)

"""
PYTHON = 1
JADE = 2
def display(type, text):
    if type == PYTHON:
        start = StartPythonPrint()
    elif type == JADE:
        start = StartJadeWrite()
    if type == PYTHON:
        end = EndPythonPrint()
    elif type == JADE:
        end = EndJadeWrite()
    print(start.get() + text + end.get())
    
print("(***Python***")
display( PYTHON, "This is a test")

print("***Jade***")
display( JADE, "This is a test")







        