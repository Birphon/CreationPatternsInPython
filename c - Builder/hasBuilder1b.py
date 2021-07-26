"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Hawaiian Pizza option mentioned at the end
"""

class PizzaBuilder(object):
    def __init__(self):
        self.ingredients = []
    def addBase(self):
        self.ingredients.append('base')
    def addMainTopping(self):
        pass
    def addCheese(self):
        pass
    def addAdditionalTopping(self):
        pass
    def getPizza(self):
        return self.ingredients
    
class VeggiePizzaBuilder(PizzaBuilder):
    def addMainTopping(self):
        self.ingredients.append("Mushrooms")
    def addCheese(self):
        self.ingredients.append("Moz")
    def addAdditionalTopping(self):
        self.ingredients.append("Sun Dried Tomatoes & Olives")

class ChickenPizzaBuilder(PizzaBuilder):
    def addMainTopping(self):
        self.ingredients.append("Chicken")
    def addCheese(self):
        self.ingredients.append("Blue Cheese")
    def addAdditionalTopping(self):
        self.ingredients.append("Capsicums")    

class HawaiianPizzaBuilder(PizzaBuilder):
    def addMainTopping(self):
        self.ingredients.append("Ham")
    def addCheese(self):
        self.ingredients.append("Cheddar cheese")
    def addAdditionalTopping(self):
        self.ingredients.append("Pineapple and Baccon")  
    def addBase(self):
        self.ingredients.append("Flakey Pastry Base")
class PizzaDirector(object):
    def __init__(self, builder):
        self.builder = builder
    def makePizza(self):
        self.builder.addBase()
        self.builder.addMainTopping()
        self.builder.addCheese()
        self.builder.addAdditionalTopping()
        return self.builder.getPizza()
        


 
pizzaMachine = PizzaDirector(VeggiePizzaBuilder())
print pizzaMachine.makePizza()
pizzaMachine.builder = ChickenPizzaBuilder()
print pizzaMachine.makePizza()
pizzaMachine.builder = HawaiianPizzaBuilder()
print pizzaMachine.makePizza()
"""additional functionality required is
        Hawaiian Pizza
        which has a Flakey Pastry Base,
        Ham as a main ingredient,
        Cheddar cheese
        and Pineapple and Baccon as the additional topping
        ['Flakey Pastry Base', 'Ham', 'Cheddar cheese', 'Pineapple and Baccon']
""" 