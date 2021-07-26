from string import *;
"""
FACTORY METHOD DEMO 
"""

class VehiclePart(object):
    def __init__(self, name):
        self.name = name;
        self.part = [];
    def __str__(self):
        s = self.name;
        if self.part:
            s = s + "(";
            for part in self.part:
                s = s + str(part) + ", ";
            s = s + ")";
        return s;
    def add(self, part):
        self.part.append(part);

class VehicleMotor(VehiclePart):
    def __init__(self, capacity):
        assert(type(capacity) == type(0));
        VehiclePart.__init__(self, "Motor with %d ccm Capacity" % capacity);
        if capacity < 1500:
            motor = MotorCycleMotor(capacity);
            for i in range(2): motor.add(MotorCycleMotorCylinder("%d" % (i+1)));
        else:
            motor = CarMotor(capacity);
            for i in range(4): motor.add(CarMotorCylinder("%d" % (i+1)));
        self = motor;

class VehicleWheel(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, "Wheel " + name);

class Vehicle(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, name);
        self.name = name;
        self.vehiclePart = [];
    def __str__(self):
        s = "this Vehicle consists of %d Parts: " % len(self.vehiclePart);
        for part in self.vehiclePart:
            s = s + str(part) + ", ";
        return s + ". ";
    def addMotor(self, motor):
        self.vehiclePart.append(motor);
    def addWheel(self, wheel):
        self.vehiclePart.append(wheel);

class CarMotor(VehiclePart):
    def __init__(self, capacity):
        VehiclePart.__init__(self, "%d" % capacity);

class CarMotorCylinder(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, name);

class CarWheel(VehicleWheel):
    def __init__(self, name):
        VehicleWheel.__init__(self, name);

class CarHub(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, name);

class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name);
    def __str__(self):
        s = "This car consists of %d Parts: " % len(self.vehiclePart);
        for Part in self.vehiclePart:
            s = s + str(Part) + ", ";
        return s + ". ";

class MotorCyclePart:
    def __init__(self, name):
        self.name = name;
        self.part = [];
    def __str__(self):
        return self.name;
    def add(self, part):
        self.part.append(part);

class MotorCycleWheel(VehicleWheel):
    def __init__(self, name):
        VehicleWheel.__init__(self, name);

class MotorCycleHub(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, name);

class MotorCycleMotor(VehiclePart):
    def __init__(self, capacity):
        VehiclePart.__init__(self, "%d" % capacity);

class MotorCycleMotorCylinder(VehiclePart):
    def __init__(self, name):
        VehiclePart.__init__(self, name);

class MotorCycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name);
    def __str__(self):
        s = "This motorcycle consists of %d Parts: " % len(self.vehiclePart);
        for Part in self.vehiclePart:
            s = s + str(Part) + ", ";
        return s + ". ";

class Factory:
    """
    Produces vehicles in individual Parts
    """
    def __init__(self):
        self.Vehicle = None;
    def produceVehicle(self, name):
        assert(not "Trapped: ABC!");
    def produceWheel(self):
        assert(not "Trapped: ABC!");
    def produceMotor(self, sCapacity):
        assert(not "Trapped: ABC!");

class CarFactory(Factory):
    """
    Produces whole car.
    """
    def __init__(self):
        Factory.__init__(self);
    def produceVehicle(self, name):
        self.Vehicle = Car(name);
    def produceMotor(self, capacity):
        assert(type(capacity) == type(0));
        motor = VehicleMotor(capacity);            # Virtual ctor
        self.Vehicle.addMotor(motor);
    def produceWheel(self):
        for i in range(4):
            self.Vehicle.addWheel(CarWheel("%d" % (i+1)));
    def supplyVehicle(self):
        return self.Vehicle;

class BikeFactory(Factory):
    """
    Produces whole motorcycle.
    """
    def __init__(self):
        Factory.__init__(self);
    def produceVehicle(self, name):
        self.Vehicle = MotorCycle(name);
    def produceMotor(self, capacity):
        motor = VehicleMotor(capacity);            # Virtual ctor
        self.Vehicle.addMotor(motor);
    def produceWheel(self):
        for i in range(2):
            self.Vehicle.addWheel(MotorCycleWheel("%d" % (i+1)));
    def supplyVehicle(self):
        return self.Vehicle;

class VehicleSalesPerson:
    """
    The Vehicle salesman does not know which Vehicle to build;
    he knows only the factory with which assembles the Vehicle.
    If he is to build another Vehicle,
    simply another factory is handed over to him.
    """
    def __init__(self, Factory): self.Factory = Factory;
    def produceVehicle(self, name, capacity):
        assert(type(capacity) == type(0));
        self.Factory.produceVehicle(name);
        self.Factory.produceMotor(capacity);
        self.Factory.produceWheel();
        return self.Factory.supplyVehicle();

def main():
    print;
    s = "FACTORY METHOD (VIRTUAL CONSTRUCTOR) Pattern"; print(s); print( "-" * len(s));
    #We can be built a car...
    vehicleSalesPerson = VehicleSalesPerson(CarFactory());
    vehicle = vehicleSalesPerson.produceVehicle("Saloon", 8000);
    print(vehicle);
    # ... and now a motorcycle
    vehicleSalesPerson = VehicleSalesPerson(BikeFactory());
    vehicle = vehicleSalesPerson.produceVehicle("Sports", 500);
    print(vehicle);

if __name__ == "__main__":
    main();
