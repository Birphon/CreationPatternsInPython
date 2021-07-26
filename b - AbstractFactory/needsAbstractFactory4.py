"""
REPLACE THIS LINE WITH YOUR NAME
"""
# There are two families of related products
# AbstractProductA
class PascalSyntax(object):
    def add():
        pass
# ConcreteProductA1
class StartPascalBlock(PascalSyntax):
    def add(self):
        print("begin")
# ConcreteProductA2
class EndPascalBlock(PascalSyntax):
    def add(self):
        print("end;")
#AbstractProductB
class JavaSyntax(object):
    def add():
        pass
# ConcreteProductB1
class StartJavaBlock(JavaSyntax):
    def add(self):
        print("{")
# ConcreteProductB2
class EndJavaBlock(JavaSyntax):
    def add(self):
        print("}")

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
PASCAL = 1
JAVA = 2
def writeProgram(type, text):
    if type == PASCAL:
        start = StartPascalBlock()
    elif type == JAVA:
        start = StartJavaBlock()
    if type == PASCAL:
        end = EndPascalBlock()
    elif type == JAVA:
        end = EndJavaBlock()
    start.add()
    print("    " + text)
    end.add()
    
print("***PASCAL***")
writeProgram( PASCAL, "This is a test")

print("***JAVA***")
writeProgram( JAVA, "This is a test")







        