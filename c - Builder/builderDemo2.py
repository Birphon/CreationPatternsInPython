"""
Purpose.  Builder design pattern demo.
Discussion.
The forte of Builder is constructing a complex object step by step.
An abstract base class declares the standard construction process,
and concrete derived classes define the appropriate implementation
for each step of the process.
In this example, "distributed work packages" have been abstracted
to be persistent and platform independent.
This means that the platform-specific mechanism 
for implementing files, queues, and concurrency pathways
is defined in each platform's concrete derived class.
A single "reader" object (i.e. parser)
retrieves the archived specification for a DistrWorkPackage
and proceeds to delegate each build step to the builder object
that was registered by the client.
Upon completion, the client retrieves the end result from the builder.
"""

File=0
Queue=1
Pathway=2

class DistrWorkPackage(object):
    def __init__(self, type):
        self.desc =  "\nDistributed Work Package for: %s" % type
    def setFile(self, f, v):
        temp =  "\n  File(%s): %s" % (f, v)
        self.desc = self.desc + temp
    def setQueue(self, q,  v ):
        temp = "\n  Queue(%s): %s" % (q, v)
        self.desc = self.desc + temp
    def setPathway(self, p, v ):
        temp = "\n  Pathway(%s): %s" % (p, v)
        self.desc = self.desc + temp
    def getState(self):
        return self.desc

class Builder(object):
    def __init__(self):
        result = None
    def configureFile(self, char ):
        pass
    def configureQueue(self, char ):
        pass
    def configurePathway(self, char ):
        pass
    def getResult(self):
        return self.result

class UnixBuilder(Builder):
    def __init__(self):
        self.result = DistrWorkPackage( "Unix" )
    def configureFile(self, name ):
        self.result.setFile( "flatFile", name )
    def configureQueue(self, queue ):
        self.result.setQueue( "FIFO", queue )
    def configurePathway(self, type ):
        self.result.setPathway( "thread", type )

class VmsBuilder(Builder):
    def __init__( self ):
        self.result = DistrWorkPackage( "Vms" )
    def configureFile( self, name ):
        self.result.setFile( "ISAM", name )
    def configureQueue( self, queue ):
        self.result.setQueue( "priority", queue )
    def configurePathway( self, type ):
        self.result.setPathway( "LWP", type )

class Reader(object):
    def setBuilder(self, b):
        self.builder = b
    def construct( self, data ):
        type= data[0]
        value= data[1]
        if type == File:
            self.builder.configureFile( value )
        elif type == Queue:
            self.builder.configureQueue( value )
        elif type == Pathway:
            self.builder.configurePathway( value )

if __name__ == "__main__":
    inputs = ((File, "state.dat"),
              (File,"config.sys"),
              (Queue, "compute"),
              (Queue, "log"),
              (Pathway, "authentication"),
              (Pathway, "error processing") )
    unixBuilder = UnixBuilder()
    vmsBuilder  = VmsBuilder()

    reader = Reader()
    reader.setBuilder( unixBuilder )
    for input in inputs:
        reader.construct( input )
    print(unixBuilder.getResult().getState())

    reader.setBuilder( vmsBuilder )
    for input in inputs:
        reader.construct( input )
    print(vmsBuilder.getResult().getState())

"""
Distributed Work Package for: Unix
  File(flatFile): state.dat
  File(flatFile): config.sys
  Queue(FIFO): compute
  Queue(FIFO): log
  Pathway(thread): authentication
  Pathway(thread): error processing

Distributed Work Package for: Vms
  File(ISAM): state.dat
  File(ISAM): config.sys
  Queue(priority): compute
  Queue(priority): log
  Pathway(LWP): authentication
  Pathway(LWP): error processing
"""
