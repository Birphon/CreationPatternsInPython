"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Hawaiian Pizza option mentioned at the end
"""

class PizzaBuilder(object): #abstract
    def __init__(self):
        self.ingedients = []
    def getResult(self):
        return self.ingedients
    def addBase(self): pass
    def addMainTopping(self): pass
    def addCheese(self): pass
    def addAdditionalTopping(self): pass


class VeggiePizzaBuilder(PizzaBuilder): #CONCRETE
    def addBase(self):
        self.ingedients.append("Soft Crust Base")
    def addMainTopping(self):
        self.ingedients.append("Mushrooms")
    def addCheese(self):
         self.ingedients.append("Moz")
    def addAdditionalTopping(self):
        self.ingedients.append("Sun Dried Tomatoes & Olives")

class ChickenPizzaBuilder(PizzaBuilder): #CONCRETE
    def addBase(self):
        self.ingedients.append("Soft Crust Base")
    def addMainTopping(self):
        self.ingedients.append("Chicken")
    def addCheese(self):
         self.ingedients.append("Blue Cheese")
    def addAdditionalTopping(self):
        self.ingedients.append("Capsicums")

class DesssertPizzaBuilder(PizzaBuilder): #CONCRETE
    def addBase(self):
        self.ingedients.append("Stuffed Crust Base")
    def addMainTopping(self):
        self.ingedients.append("Chocolate")
    def addCheese(self):
         self.ingedients.append("Cream Cheese")
    def addAdditionalTopping(self):
        self.ingedients.append("Hundreds and Thousands")
    
class PizzaArchitectChef(object):
    def __init__(self, pizzaBuilder):
        self.pizzaBuilder = pizzaBuilder
    def construct(self):
        self.pizzaBuilder.addBase()
        self.pizzaBuilder.addMainTopping()
        self.pizzaBuilder.addCheese()
        self.pizzaBuilder.addCheese()
        self.pizzaBuilder.addAdditionalTopping()
        return self.pizzaBuilder.getResult()
        
    


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
    #chickenPizzaMachine = PizzaKitMatic("Chicken")
    print(PizzaArchitectChef(ChickenPizzaBuilder()).construct())
    #['Soft Crust Base', 'Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']
    
    #veggiePizzaMachine = PizzaKitMatic("Veggie")
    print( PizzaArchitectChef( VeggiePizzaBuilder() ).construct() )
    #['Soft Crust Base', 'Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']

    print( PizzaArchitectChef( DesssertPizzaBuilder() ).construct() )

    """additional functionality required is
        Hawaiian Pizza
        which has a Flakey Pastry Base,
        Ham as a main ingredient,
        Cheddar cheese
        and Pineapple and Baccon as the additional topping
        ['Flakey Pastry Base', 'Ham', 'Cheddar cheese', 'Pineapple and Baccon']
    """ 