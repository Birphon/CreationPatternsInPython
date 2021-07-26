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

def createUnixSocket():
    print("createUnixSocket:")
    
def createVmsSocket():
    print("createVmsSocket:")
    
def createNtSocket():
    print("createNtSocket:")
    
def createUnixPipe():
    print("createUnixPipe:")
    
def createVmsPipe():
    print("createVmsPipe:")
    
def createNtPipe():
    print("createNtPipe:")
    
def createUnixThread():
    print("createUnixThread:")
    
def createVmsThread():
    print("createVmsThread:")
    
def createNtThread():
    print("createNtThread:")


def doOneLaneIPC():
    if UNIX:
        createUnixSocket()
    elif VMS:
        createVmsSocket()
    elif NT:
        createNtSocket()

def doTwoLaneIPC():
    if UNIX:
        createUnixPipe()
    elif VMS:
        createVmsPipe()
    elif NT:
       createNtPipe()


def doParallelProcessing():
    if UNIX:
       createUnixThread()
    elif VMS:
        createVmsThread()
    elif NT:
        createNtThread()


if __name__ == "__main__":
    VMS = 1
    UNIX = 0
    NT = 0
    doOneLaneIPC()
    doTwoLaneIPC()
    doParallelProcessing()
    print("main: complete")

"""
-- current output --
 createVmsSocket:
 createVmsPipe:
 createVmsThread:
 main: complete

 -- target output --
 VmsFactory: createSocket
 VmsFactory: createPipe
 VmsFactory: createThread
 main: complete
"""