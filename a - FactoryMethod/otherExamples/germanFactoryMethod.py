from string import *;


"""
Musste bei den Patterns ABSTRACT FACTORY und BUILDER die Auto- bzw. Bike-Fabrik wissen,
welchen Motor sie auswaehlen muss und wie viele Zylinder er hat, so wollen wir das nun
den Motor selbst "entscheiden" lassen - in Abhaengigkeit vom Hubraum. Die Fabrik
gibt nun nur noch einen Motor in Auftrag, die Motor-Klasse erzeugt dann den richtigen Motor.
"""


class TKFZTeil:
    def __init__(self, sName):
        self.sName = sName;
        self.aTeil = [];

    def __str__(self):
        s = self.sName;
        if self.aTeil:
            s = s + "(";
            for teil in self.aTeil:
                s = s + str(teil) + ", ";
            s = s + ")";
        return s;

    def Add(self, teil):
        self.aTeil.append(teil);

class TKFZMotor(TKFZTeil):
    def __init__(self, iHubraum):
        assert(type(iHubraum) == type(0));
        TKFZTeil.__init__(self, "Motor mit %d ccm Hubraum" % iHubraum);
        if iHubraum < 1500:
            motor = TBikeMotor(iHubraum);
            for i in range(2): motor.Add(TBikeMotorZylinder("%d" % (i+1)));
        else:
            motor = TAutoMotor(iHubraum);
            for i in range(4): motor.Add(TAutoMotorZylinder("%d" % (i+1)));
        self = motor;


class TKFZRad(TKFZTeil):
    def __init__(self, sName): TKFZTeil.__init__(self, "Rad " + sName);

class TKFZ(TKFZTeil):
    def __init__(self, sName):
        TKFZTeil.__init__(self, sName);
        self.sName = sName;
        self.aKFZTeil = [];

    def __str__(self):
        s = "Dieses KFZ besteht aus %d Teilen: " % len(self.aKFZTeil);
        for teil in self.aKFZTeil:
            s = s + str(teil) + ", ";
        return s + ". ";

    def AddMotor(self, Motor):
        self.aKFZTeil.append(Motor);

    def AddRad(self, Rad):
        self.aKFZTeil.append(Rad);


#class TAutoMotor(TKFZTeil):
#    def __init__(self, iHubraum): TKFZTeil.__init__(self, "%d" % iHubraum);
class TAutoMotor(TKFZTeil):
    def __init__(self, iHubraum): TKFZTeil.__init__(self, "%d" % iHubraum);

class TAutoMotorZylinder(TKFZTeil):
    def __init__(self, sName): TKFZTeil.__init__(self, sName);

class TAutoRad(TKFZRad):
    def __init__(self, sName): TKFZRad.__init__(self, sName);

class TAutoRadFelge(TKFZTeil):
    def __init__(self, sName): TKFZTeil.__init__(self, sName);

class TAuto(TKFZ):
    def __init__(self, sName): TKFZ.__init__(self, sName);

    def __str__(self):
        s = "Dieses Auto besteht aus %d Teilen: " % len(self.aKFZTeil);
        for teil in self.aKFZTeil:
            s = s + str(teil) + ", ";
        return s + ". ";

class TBiketeil:
    def __init__(self, sName):
        self.sName = sName;
        self.aTeil = [];

    def __str__(self):
        return self.sName;

    def Add(self, teil):
        self.aTeil.append(teil);

class TBikeRad(TKFZRad):
    def __init__(self, sName): TKFZRad.__init__(self, sName);

class TBikeRadFelge(TKFZTeil):
    def __init__(self, sName): TKFZTeil.__init__(self, sName);

class TBikeMotor(TKFZTeil):
    def __init__(self, iHubraum): TKFZTeil.__init__(self, "%d" % iHubraum);

class TBikeMotorZylinder(TKFZTeil):
    def __init__(self, sName): TKFZTeil.__init__(self, sName);

class TBike(TKFZ):
    def __init__(self, sName): TKFZ.__init__(self, sName);

    def __str__(self):
        s = "Dieses Motorrad besteht aus %d Teilen: " % len(self.aKFZTeil);
        for teil in self.aKFZTeil:
            s = s + str(teil) + ", ";
        return s + ". ";


class TFabrik:
    """
    Erzeugt 4-raedrige KFZs in Einzelteilen(!).
    """
    def __init__(self):
        self.KFZ = None;

    def ErzeugeKFZ(self, sName):
        assert(not "Trapped: ABC!");

    def ErzeugeRaeder(self):
        assert(not "Trapped: ABC!");

    def ErzeugeMotor(self, sHubraum):
        assert(not "Trapped: ABC!");

class TFabrik4Autos(TFabrik):
    """
    Erzeugt ganzes Auto.
    """
    def __init__(self):
        TFabrik.__init__(self);

    def ErzeugeKFZ(self, sName):
        self.KFZ = TAuto(sName);

    def ErzeugeMotor(self, iHubraum):
        assert(type(iHubraum) == type(0));
        motor = TKFZMotor(iHubraum);            # Virtual ctor
        self.KFZ.AddMotor(motor);

    def ErzeugeRaeder(self):
        for i in range(4):
            self.KFZ.AddRad(TAutoRad("%d" % (i+1)));

    def LiefereKFZ(self):
        return self.KFZ;

class TFabrik4Bikes(TFabrik):
    """
    Erzeugt ganzes Motorrad.
    """
    def __init__(self): TFabrik.__init__(self);

    def ErzeugeKFZ(self, sName):
        self.KFZ = TBike(sName);

    def ErzeugeMotor(self, iHubraum):
        motor = TKFZMotor(iHubraum);            # Virtual ctor
        self.KFZ.AddMotor(motor);

    def ErzeugeRaeder(self):
        for i in range(2):
            self.KFZ.AddRad(TBikeRad("%d" % (i+1)));

    def LiefereKFZ(self):
        return self.KFZ;


class TKFZVerkaufer:
    """
    Der KFZ-Verkaeufer weiss nicht, welches KFZ er baut; er weiss nur, was
    die Fabrik kann, mit der er das KFZ zusammenbaut.
    Soll er ein anderes KFZ bauen, wird ihm einfach eine andere Fabrik uebergeben.
    """
    def __init__(self, Fabrik): self.Fabrik = Fabrik;

    def ErzeugeKFZ(self, sName, iHubraum):
        assert(type(iHubraum) == type(0));
        self.Fabrik.ErzeugeKFZ(sName);
        self.Fabrik.ErzeugeMotor(iHubraum);
        self.Fabrik.ErzeugeRaeder();
        return self.Fabrik.LiefereKFZ();


def main():
    print;
    s = "FACTORY METHOD (VIRTUAL CTOR) Pattern"; print(s); print( "-" * len(s));
    #
    # Wir lassen uns ein Auto bauen...
    kfzverkaeufer = TKFZVerkaufer(TFabrik4Autos());
    kfz = kfzverkaeufer.ErzeugeKFZ("Schlitten", 8000);
    print(kfz);
    #
    # ... und jetzt ein Motorrad
    kfzverkaeufer = TKFZVerkaufer(TFabrik4Bikes());
    kfz = kfzverkaeufer.ErzeugeKFZ("Renner", 500);
    print(kfz);

if __name__ == "__main__":
    main();
