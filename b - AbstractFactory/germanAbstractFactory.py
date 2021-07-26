from string import *
"""
ABSTRACT FRACTORY DEMO
"""

class Computer(object):
    def __init__(self):
        self.__cabinet = None
        self.__monitor = None
        self.__hdd = None
        self.__motherboard = None
        self.__processor = None
        self.__ram = None
        self.__keyboard = None
    def addCabinet(self, cabinet):
        self.__cabinet = cabinet
    def addMonitor(self, monitor):
        self.__monitor = monitor
    def addHDD(self, hdd):
        self.__hdd = hdd
    def addMotherboard(self, motherboard):
        self.__motherboard = motherboard
    def addProcessor(self, processor):
        self.__processor = processor
    def addRAM(self, ram):
        self.__ram = ram
    def addKeyboard(self, keyboard):
        self.__keyboard = keyboard
    def __str__(self):
        return ' '.join(map(str, [self.__cabinet, self.__monitor, self.__hdd, self.__motherboard, self.__processor, self.__ram, self.__keyboard]))

class Case(object):
    def __init__(self, kind="Midi Tower"):
        self.__kind = kind
    def __str__(self):
        return self.__kind

class Monitor(object):
    def __init__(self, sizeInches):
        if self.__class__ == Monitor:
            raise TypeError('Monitor')
        self._size = sizeInches
    def __str__(self):
        raise NotImplementedError(' __str__')

class CRTMonitor(Monitor):
    def __init__(self, sizeInches):
        Monitor.__init__(self, sizeInches)
    def __str__(self):
        return "CRT Monitor, %d inches of size" % self._size

class LCDMonitor(Monitor):
    def __init__(self, sizeInches):
        Monitor.__init__(self, sizeInches)
    def __str__(self):
        return "LCD Monitor, %d inches of size" % self._size

class HardDrive:
    def __init__(self, sizeGB):
        self.__size = sizeGB
    def __str__(self):
        return "%d GB" % self.__size

class Motherboard(object):
    def __init__(self, numProcessors):
        self.__numProcessors = numProcessors
    def __str__(self):
        return "Motherboard for %d processors" % self.__numProcessors

class Processor(object):
    def __init__(self, freq):
        self.__freq = freq
    def __str__(self):
        return "%d MHz Processor" % self.__freq

class RAM(object):
    def __init__(self, sizeMB):
        self.__size = sizeMB
    def __str__(self):
        return "%d MB of memory" % self.__size

class Keyboard(object):
    def __init__(self):
        pass
    def __str__(self):
        return "Keyboard"

class ComputerFactory(object):
    def __init__(self):
        if self.__class__ == ComputerFactory:
            raise TypeError('ComputerFactory')
    def makeComputer(self):
        raise NotImplementedError()
    def makeCabinet(self):
        raise NotImplementedError()
    def makeMonitor(self):
        raise NotImplementedError()
    def makeHDD(self):
        raise NotImplementedError()
    def makeMotherboard(self):
        raise NotImplementedError()
    def makeProcessor(self):
        raise NotImplementedError()
    def makeRAM(self):
        raise NotImplementedError()
    def makeKeyboard(self):
        raise NotImplementedError()

class ServerFactory(ComputerFactory):
    def __init__(self):
        ComputerFactory.__init__(self)
    def makeComputer(self):
        return Computer()
    def makeCabinet(self):
        return Case("Tower")
    def makeMonitor(self):
        return CRTMonitor(15)
    def makeHDD(self):
        return HardDrive(70)
    def makeMotherboard(self):
        return Motherboard(4)
    def makeProcessor(self):
        return Processor(1000)
    def makeRAM(self):
        return RAM(1000)
    def makeKeyboard(self):
        return Keyboard()


class WorkstationFactory(ComputerFactory):
    def __init__(self):
        ComputerFactory.__init__(self)
    def makeComputer(self):
        return Computer()
    def makeCabinet(self):
        return Case("Mini Tower")
    def makeMonitor(self):
        return CRTMonitor(20)
    def makeHDD(self):
        return HardDrive(20)
    def makeMotherboard(self):
        return Motherboard(1)
    def makeProcessor(self):
        return Processor(1000)
    def makeRAM(self):
        return RAM(256)
    def makeKeyboard(self):
        return Keyboard()

class ITEquipment(object):
    def __init__(self):
        self.__aComputer = []
    def createComputer(self, factory):
        """ SYNOPSIS:
                The 'factory' delivers the container and all the parts.
                This method assembles them all into the container using
                the container's functionality.
        """
        computer = Computer()
        computer.addCabinet(factory.makeCabinet())
        computer.addMonitor(factory.makeMonitor())
        computer.addHDD(factory.makeHDD())
        computer.addMotherboard(factory.makeMotherboard())
        computer.addProcessor(factory.makeProcessor())
        computer.addRAM(factory.makeRAM())
        computer.addKeyboard(factory.makeKeyboard())
        return computer
    def addComputer(self, computer):
        self.__aComputer.append(computer)
    def computers(self):    return self.__aComputer

def main():
    """ Now we tell our equipment to assemble the computers we
        want to have it contain. For this we simply have to hand over the
        appropriate factories.
    """
    equipment = ITEquipment()
    equipment.addComputer(equipment.createComputer(ServerFactory()))
    equipment.addComputer(equipment.createComputer(WorkstationFactory()))

    print("My IT-Equipment consists of:")
    for each in equipment.computers():
        print(each)
    """ DISCUSSION:
            The knowledge of which components a certain computer consists of
            is hidden in the factory methods.
            The knowledge of how to assemble a certain computer
            is hidden in ITEquipment::createComputer().
            To create a computer,
            ITEquipment does not need to know
            the concrete classes of all the components
            making up a computer.
    """

main()