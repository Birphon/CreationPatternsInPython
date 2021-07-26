"""
Purpose.  Abstract Factory design pattern lab.
 
Problem.
case statements are spread throughout the code to accomodate 3 different porting targets.
This makes maintenance difficult, and porting to a 4th platform onerous.

Assignment.
 1. Create an abstract base class Factory.
 2. In this base Factory class define member functions createSocket(), createPipe(),
   and createThread(). All are 'pass' abstract functions.
 3. Subclass UnixFactory, VmsFactory, and NtFactory off of Factory.
 4. Refactor the "create" functions to be member functions of one of
   the Factory derived classes.
 5. Declare a factory pointer local to "__main__"
 6. Use a single if case statement in "__main__" to instantiate the desired
   Factory derived class.
 7. Do not optimize-out the doOneLaneIPC(), doTwoLaneIPC(), and
   doParallelProcessing() free functions.
 8. Pass the Factory pointer to each of these free functions so that they
   can create sockets, pipes, and threads without regard to race, creed,
   or platform.
 9. Extra credit: implement the Factory class as a Singleton.
"""
class Factory(object):
    def createSocket(self):
        pass
    def createPipe(self):
        pass
    def createThread(self):
        pass

class UnixFactory(Factory):
    def createSocket(self):
        print "UnixFactory: createSocket:"
    def createPipe(self):
        print "UnixFactory: createPipe:"
    def createThread(self):
        print "UnixFactory: createThread:"

class NtFactory(Factory):
    def createSocket(self):
        print "NtFactory: createSocket:"
    def createPipe(self):
        print "NtFactory: createPipe:"
    def createThread(self):
        print "NtFactory: createThread:"

class VmsFactory(Factory):
    def createSocket(self):
        print "VmsFactory: createSocket:"
    def createPipe(self):
        print "VmsFactory: createPipe:"
    def createThread(self):
        print "VmsFactory: createThread:"

def doOneLaneIPC(factory):
    factory.createSocket()

def doTwoLaneIPC(factory):
    factory.createPipe()

def doParallelProcessing(factory):
    factory.createThread()


if __name__ == "__main__":
    VMS = True
    UNIX = False
    NT = False
    if UNIX:
       f = UnixFactory()
    elif VMS:
        f = VmsFactory()
    elif NT:
        f = NtFactory();
    doOneLaneIPC(f)
    doTwoLaneIPC(f)
    doParallelProcessing(f)
    print "main: complete"

"""
 VmsFactory: createSocket
 VmsFactory: createPipe
 VmsFactory: createThread
 main: complete
"""