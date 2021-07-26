"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Hawaiian Pizza option mentioned at the end
"""

class PizzaShop(object): # DIRECTOR
    def __init__(self, builder):
        self.builder = builder
    def makePizza(self): # construct
        self.builder.addBase()
        self.builder.addTopping()
        self.builder.addCheese()
        self.builder.addExtras()
        return self.builder.getResult()
    
class Pizza(object): # abstruct builder
    def __init__(self):
        self.ingedients = []
    def addBase(self):
        self.ingedients.append("Soft Crust Base")  
    def addTopping(self):pass
    def addCheese(self):pass
    def addExtras(self):pass
    def getResult(self):
        return self.ingedients
    
class ChickenPizza(Pizza):
    def addTopping(self):
         self.ingedients.append("Chicken")
    def addCheese(self):
        self.ingedients.append("Blue Cheese")
    def addExtras(self):
        self.ingedients.append("Capsicums")

class VeggiePizza(Pizza):
    def addTopping(self):
         self.ingedients.append("Mushrooms")
    def addCheese(self):
        self.ingedients.append("Moz")
    def addExtras(self):
        self.ingedients.append("Sun Dried Tomatoes & Olives")    
        


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
    chickenPizzaMachine = PizzaShop( ChickenPizza() )
    print(chickenPizzaMachine.makePizza())
    #['Soft Crust Base', 'Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']
    
    veggiePizzaMachine = PizzaShop( VeggiePizza() )  #    chickenPizzaMachine.builder = VeggiePizza()
    print(veggiePizzaMachine.makePizza())
    #['Soft Crust Base', 'Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']
    
    """additional functionality required is
        Hawaiian Pizza
        which has a Flakey Pastry Base,
        Ham as a main ingredient,
        Cheddar cheese
        and Pineapple and Baccon as the additional topping
        ['Flakey Pastry Base', 'Ham', 'Cheddar cheese', 'Pineapple and Baccon']
    """ 