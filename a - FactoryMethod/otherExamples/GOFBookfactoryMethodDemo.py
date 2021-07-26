# factoryMethodDemo2.py
"""
Purpose.
Factory Method design pattern demo.
Discussion:
 Frameworks are applications (or subsystems) with "holes" in them.
 Each framework specifies the infrastructure, superstructure,
 and flow of control for its "domain",
 and the client of the framework may:
     exercise the framework's default behavior "as is",
     extend selected pieces of the framework,
     or replace selected pieces.
 The Factory Method pattern addresses the notion of "creation"
 in the context of frameworks.
 In this example,
 the framework knows WHEN a new document should be created,
 not WHAT kind of Document to create.
 The "placeholder" Application::CreateDocument()
 has been declared by the framework,
 and the client is expected to "fill in the blank" for his/her specific document(s).
 Then, when the client asks for Application::NewDocument(),
 the framework will subsequently call the client's MyApplication::CreateDocument().

USAGE:
# Client's customization of the Framework

>>> myApp = MyApplication()
MyApplication: init
Application: init
>>> myApp.newDocument( "foo" );
Application: NewDocument()
   MyApplication: CreateDocument()
   MyDocument: Open()
>>> myApp.newDocument( "bar" );
Application: NewDocument()
   MyApplication: CreateDocument()
   MyDocument: Open()
>>> myApp.reportDocs();
Application: ReportDocs()
   foo
   bar
"""
class Document(object):
    """ Abstract base class declared by framework """
    def __init__(self, name):
        self.name = name
    def open(self):
        raise NotImplementedError 
    def close(self):
        raise NotImplementedError
    def getName(self):
        return self.name

class Application(object):
    """ Framework declaration """
    def __init__(self):
        self.docs = []
        print("Application: init")
    def createDocument(self, name):
        """ Framework declares a "hole" for the client to customize """
        pass
    def newDocument(self, name):
        # The client will call this "entry point" of the framework 
        # Framework calls the "hole" reserved for client customization 
        print("Application: NewDocument()")
        doc = self.createDocument(name)
        self.docs.append(doc)
        doc.open()
    def reportDocs(self):
        print("Application: ReportDocs()" )
        for document in self.docs:
            print( "   " + document.getName())

class MyDocument(Document):
    """  Concrete derived class defined by client """
    def open(self):
        print("   MyDocument: Open()")
    def close(self):
        print("   MyDocument: Close()")

class MyApplication(Application):
    """ Customization of framework defined by client """
    def __init__(self):
        print("MyApplication: init")
        Application.__init__(self)
    def createDocument(self,name):
        """ Client defines Framework's hole """
        print("   MyApplication: CreateDocument()")
        return MyDocument(name)

def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()