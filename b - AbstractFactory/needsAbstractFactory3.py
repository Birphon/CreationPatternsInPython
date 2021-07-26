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
and know all about the markup choices

Change things by applying the ABSTRACT FACTORY pattern
so the client only has to decide the type of feast
and does not need to know the details of markup preparation.

To make things simplier can you please ..
get rid of the constants (too much to remember)
get rid of the case statements (too difficult to maintain)

"""

"""
XHTML = 1
HTML = 2

def markup(type, text):
	if type == XHTML:
		startTag = StartParaTag()
	elif type == HTML:
		startTag = StartP()
	if type == XHTML:
		endTag = EndParaTag()
	elif type == HTML:
		endTag = End()
	print(startTag.show() + text + endTag.show())
"""
class AbstractFactory:
	def makeStartParaTag(): pass
	def makeEndParaTag(): pass
	
class XHTML_Factory: 
	def makeStartParaTag(): 
		return StartParaTag()
	def makeEndParaTag(): 
		return EndParaTag()
	
class HTML_Factory:
	def makeStartParaTag(): 
		return StartP()
	def makeEndParaTag(): 
		return End()


class Client:
	def __init__(self, concrete_factory):
		self.factory = concrete_factory
	
	def markup(self, text):
		startTag = self.factory.makeStartParaTag()
		endTag = self.factory.makeEndParaTag()
		print(startTag.show() + text + endTag.show())
    
print("***xhtml***")
client = Client(XHTML_Factory())
client.markup("This is a test")
client.markup("This is a another test")
print("***html***")
client = Client(HTML_Factory())
client.markup("This is a test")
client.markup("This is a another test")






        