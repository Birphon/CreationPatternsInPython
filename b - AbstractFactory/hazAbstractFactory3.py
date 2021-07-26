"""
REPLACE THIS LINE WITH YOUR NAME
"""
# There are two families of related products
# AbstractProductA
class XHTMLtag(object):
    def show():
        pass
# ConcreteProductA1
class StartParaTag(XHTMLtag):
    def show(self):
        return "<p>"
# ConcreteProductA2
class EndParaTag(XHTMLtag):
    def show(self):
        return "</p>"
#AbstractProductB
class HTMLtag(object):
    def show():
        pass
# ConcreteProductB1
class StartP(HTMLtag):
    def show(self):
        return "<P>"
# ConcreteProductB2
class End(HTMLtag):
    def show(self):
        return ""

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
XHTML = 1
HTML = 2

class AbstractFactory(object):
    def makeStartTag(self):pass
    def makeEndTag(self):pass
class XHTMLFactory(AbstractFactory):
    def makeStartTag(self):return StartParaTag()
    def makeEndTag(self): return EndParaTag()
class HTMLFactory(AbstractFactory):
    def makeStartTag(self):return StartP()
    def makeEndTag(self): return End()    

def markup(factory, text):
    startTag = factory.makeStartTag()
    endTag = factory.makeEndTag()
    print(startTag.show() + text + endTag.show())
    
print("***xhtml***")
markup( XHTMLFactory(), "This is a test")
markup( XHTMLFactory(), "This is a another test")
print("***html***")
markup( HTMLFactory(), "This is a test")
markup( HTMLFactory(), "This is a another test")






        