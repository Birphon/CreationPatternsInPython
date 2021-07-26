class TPrinter:
    def __init__(self, sId):
        self.sId = sId

    def printout(self, sFfn):
        print "%s is printing %s..." % (self.sId, sFfn)


class TPrinterHP(TPrinter):
    def __init__(self, sModel):
        TPrinter.__init__(self, "HP %s" % sModel)


class TPrinterPool:

    def __init__(self):
        self.hs2prn = {}

    def addPrinter(self, sName, printer):
        self.hs2prn[sName] = printer

    def printer(self, sName):
        return self.hs2prn[sName]

    def numPrinters(self):
        return len(self.hs2prn.items())

__singleTPrinterPool = TPrinterPool() # The only one, created once

def makePrinterPool():
    return __singleTPrinterPool

TPrinterPool = makePrinterPool


def configPrinters():
    print
    pool = TPrinterPool()
    print "# of printers before configuration: %d" % pool.numPrinters()
    pool.addPrinter("Printer on 2nd floor", TPrinterHP("Laserjet 5L"))
    pool.addPrinter("Printer on 3rd floor", TPrinterHP("Laserjet 1100"))
    print "# of printers after configuration: %d" % pool.numPrinters()


def printSomething():
    print
    pool = TPrinterPool()
    print "# of printers available: %d" % pool.numPrinters()
    pool.printer("Printer on 2nd floor").printout("D:\\MyDocs\\This.doc")
    pool.printer("Printer on 3rd floor").printout("D:\\MyDocs\\That.doc")


def main():
    print
    configPrinters()
    printSomething()

    pool = TPrinterPool()
    pool.printer("Printer on 3rd floor").printout("D:\\MyDocs\\AndThisOneToo.doc")

main()
"""
Eine interessante Realisierung des Singleton-Patterns findet sich bei Peter Norvig . Interessant deswegen, weil diese Variante der dynamischen Natur von Python gerecht wird resp. diese ausnützt. 


class SingletonError(Exception): pass


def _singleton(object, instantiated=[]):
   if object.__class__ in instantiated:
      raise SingletonError
   instantiated.append(object.__class__)
   return


class MySingleton:
   def __init__(self, *args):
      _singleton(self)
      :
      :
      :
      return

"""