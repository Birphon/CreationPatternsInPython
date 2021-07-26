"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Hawaiian Pizza option mentioned at the end
"""

class PizzaBuilder(object):
    def __init__(self):
        self.ingedients = []
    def addBase(self):
        pass
    def addMain(self):
        pass
    def addTopping(self):
        pass
    def addExtras(self):
        pass
    def getResult(self):
        return self.ingedients

class VeggiePizzaBuilder(PizzaBuilder):
    def addBase(self):
        self.ingedients.append("Soft Crust Base")
    def addMain(self):
        self.ingedients.append("Mushrooms")
    def addTopping(self):
        self.ingedients.append("Moz")
    def addExtras(self):
        self.ingedients.append("Sun Dried Tomatoes & Olives")   

class ChickenPizzaBuilder(PizzaBuilder):
    def addBase(self):
        self.ingedients.append("Soft Crust Base")
    def addMain(self):
        self.ingedients.append("Chicken")
    def addTopping(self):
        self.ingedients.append("Blue Cheese")
    def addExtras(self):
        self.ingedients.append("Capsicums")   


class Director(object):
    def __init__(self, builder):
        self.builder = builder
    def makePizza(self):
        self.builder.addBase()
        self.builder.addMain()
        self.builder.addTopping()
        self.builder.addExtras()
        return self.builder.getResult()
        
  
class PizzaKitMatic(object):
    def __init__(self, type):
        self.type = type
        self.ingedients = []
    def makePizza(self):
        """This design is inflexible.
            The case statement in this method
            will forever have to be edited and extended
            as new types of pizzas are added to the range.
        """
        self.ingedients.append("Soft Crust Base")
        # add main topping
        if self.type == 'Veggie':
            self.ingedients.append("Mushrooms")
        elif self.type == 'Chicken':
            self.ingedients.append("Chicken")
        # add cheese
        if self.type == 'Veggie':
            self.ingedients.append("Moz")
        elif self.type == 'Chicken':
            self.ingedients.append("Blue Cheese")
        # add additional topping
        if self.type == 'Veggie':
            self.ingedients.append("Sun Dried Tomatoes & Olives")
        elif self.type == 'Chicken':
            self.ingedients.append("Capsicums")
        return self.ingedients

if __name__ == "__main__":
    chickenPizzaMachine = Director(ChickenPizzaBuilder())
    print(chickenPizzaMachine.makePizza())
    #['Chicken', 'Blue Cheese', 'Capsicums']
"""   
    veggiePizzaMachine = PizzaKitMatic("Veggie")
    print veggiePizzaMachine.makePizza()
    #['Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']
"""
"""additional functionality required is
        Hawaiian Pizza
        which has a Flakey Pastry Base,
        Ham as a main ingredient,
        Cheddar cheese
        and Pineapple and Baccon as the additional topping
    """ 