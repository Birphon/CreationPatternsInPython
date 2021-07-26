class TKFZTeil(object):
    def __init__(self, sName):
        self.sName = sName
        self.aTeil = []
    def __str__(self):
        s = self.sName
        if self.aTeil:
            s += "("
            for teil in self.aTeil:
                s += str(teil) + ", "
            s + ")"
        return s
    def add(self, teil):
        self.aTeil.append(teil)

class TKFZMotor(TKFZTeil):
    def __init__(self, sName):
        TKFZTeil.__init__(self, "Motor mit " + sName)
class TKFZRad(TKFZTeil):
    def __init__(self, sName):
        TKFZTeil.__init__(self, "Rad " + sName)
class TKFZ(TKFZTeil):
    def __init__(self, sName):
        TKFZTeil.__init__(self, sName)
        self.sName = sName
        self.aKFZTeil = []
    def __str__(self):
        s = "Dieses KFZ besteht aus %d Teilen: " % len(self.aKFZTeil)
        for teil in self.aKFZTeil:
            s += str(teil) + ", "
        return s 
    def addMotor(self, Motor):
        self.aKFZTeil.append(Motor)
    def addRad(self, Rad):
        self.aKFZTeil.append(Rad)

class TAutoMotor(TKFZMotor): pass
class TAutoMotorZylinder(TKFZTeil):pass
class TAutoRad(TKFZRad): pass
class TAutoRadFelge(TKFZTeil):pass

class TAuto(TKFZ):
    def __str__(self):
        s = "Dieses Auto besteht aus %d Teilen: " % len(self.aKFZTeil)
        for teil in self.aKFZTeil:
            s += str(teil) + ", "
        return s 

class TBiketeil(object):
    def __init__(self, sName):
        self.sName = sName
        self.aTeil = []
    def __str__(self):
        return self.sName
    def add(self, teil):
        self.aTeil.append(teil)

class TBikeRad(TKFZRad):pass
class TBikeRadFelge(TKFZTeil):pass
class TBikeMotor(TKFZMotor):pass
class TBikeMotorZylinder(TKFZTeil):pass

class TBike(TKFZ):
    def __str__(self):
        s = "Dieses Motorrad besteht aus %d Teilen: " % len(self.aKFZTeil)
        for teil in self.aKFZTeil:
            s += str(teil) + ", "
        return s 
class TFabrik(object):
    """
    Erzeugt 4-raedrige KFZs in Einzelteilen(!).
    """
    def __init__(self):
        self.KFZ = None
    def ErzeugeKFZ(self, sName):
        assert(not "Trapped: ABC!")
    def ErzeugeRaeder(self):
        assert(not "Trapped: ABC!")
    def ErzeugeMotor(self, sHubraum):
        assert(not "Trapped: ABC!")

class TFabrik4Autos(TFabrik):
    """
    Erzeugt ganzes Auto.
    """
    def __init__(self):
        TFabrik.__init__(self)
    def ErzeugeKFZ(self, sName):
        self.KFZ = TAuto(sName)
    def ErzeugeMotor(self, sHubraum):
        motor = TAutoMotor(sHubraum)
        motor.add(TAutoMotorZylinder("Zylinder 1"))
        motor.add(TAutoMotorZylinder("Zylinder 2"))
        motor.add(TAutoMotorZylinder("Zylinder 3"))
        motor.add(TAutoMotorZylinder("Zylinder 4"))
        self.KFZ.addMotor(motor)
    def ErzeugeRaeder(self):
        for i in range(4):
            self.KFZ.addRad(TAutoRad("%d" % (i+1)))
    def LiefereKFZ(self):
        return self.KFZ

class TFabrik4Bikes(TFabrik):
    """
    Erzeugt ganzes Motorrad.
    """
    def __init__(self):
        TFabrik.__init__(self)
    def ErzeugeKFZ(self, sName):
        self.KFZ = TBike(sName)
    def ErzeugeMotor(self, sHubraum):
        motor = TBikeMotor(sHubraum)
        motor.add(TBikeMotorZylinder("Zylinder 1"))
        motor.add(TBikeMotorZylinder("Zylinder 2"))
        self.KFZ.addMotor(motor)
    def ErzeugeRaeder(self):
        for i in range(2):
            self.KFZ.addRad(TBikeRad("%d" % (i+1)))
    def LiefereKFZ(self):
        return self.KFZ


class TKFZVerkaufer(object):
    """
    Der KFZ-Verkaeufer weiss nicht, welches KFZ er baut; er weiss nur, was
    die Fabrik kann, mit der er das KFZ zusammenbaut.
    Soll er ein anderes KFZ bauen, wird ihm einfach eine andere Fabrik uebergeben.
    """
    def __init__(self, Fabrik):
        self.Fabrik = Fabrik
    def ErzeugeKFZ(self, sName, sHubraum):
        self.Fabrik.ErzeugeKFZ(sName)
        self.Fabrik.ErzeugeMotor(sHubraum)
        self.Fabrik.ErzeugeRaeder()
        return self.Fabrik.LiefereKFZ()

if __name__ == "__main__":
    print("BUILDER Pattern\n---------------")
    # Wir lassen uns ein Auto bauen...
    kfzverkaeufer = TKFZVerkaufer(TFabrik4Autos())
    print(kfzverkaeufer.ErzeugeKFZ("Schlitten", "8000 ccm"))
    # ... und jetzt ein Motorrad
    kfzverkaeufer = TKFZVerkaufer(TFabrik4Bikes())
    print(kfzverkaeufer.ErzeugeKFZ("Renner", "500 ccm"))
    # Konklusion:
    # Im Unterschied zur ABSTRACT FACTORY laesst sich beim BUILDER
    # der Client nicht die Einzelteile eines groesseren Ganzen erzeugen, um
    # sie dann selbst zusammenbauen zu muessen,
    # sondern der Client laesst sich vom Builder gleich
    # das GANZE groessere Ganze zusammenbauen.
    # Der Vorgang des Zusammenbaus wird also in die
    # Fabrik verlagert.