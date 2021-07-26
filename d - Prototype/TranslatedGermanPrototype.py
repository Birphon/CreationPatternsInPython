from string import *
from types import *

"""
By means of PROTOTYPE Pattern
a configurable factory can be created.
i.e.. there is now only a factory,
however depending on the way you configure it
different computers can be manufactured
BUGGED - does not work!! :-(
"""

class ComputerComponent(object):
    def __init__(self, name):
        self.name = name
        self.components = []
    def __str__(self):
        s = self.name
        if self.components:
            s = s + "("
            for each in self.components:
                s = s + str(each) + ", "
            s = s + ")"
        return s
    def add(self, component):
        self.components.append(component)

class ComputerProcessor(ComputerComponent):
    def __init__(self, frequency):
        assert(type(frequency) == IntType)
        if frequency < 450:
            processor = ComputerProcessorPentiumII(frequency)
        else:
            processor = ComputerProcessorPentiumIII(frequency)
        self = processor

class ComputerProcessorPentiumII(ComputerProcessor):
    def __init__(self, frequency):
        ComputerComponent.__init__(self, frequency)

class ComputerProcessorPentiumIII(ComputerProcessor):
    def __init__(self, frequency):
        ComputerComponent.__init__(self, frequency)

def main():
    print ComputerProcessor(400)
    print ComputerProcessor(500)


if __name__ == "__main__":
    main()


