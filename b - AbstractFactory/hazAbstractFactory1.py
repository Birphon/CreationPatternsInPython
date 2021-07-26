"""
REPLACE THIS LINE WITH YOUR NAME

NEEDS ABSTRACT FACTORY

"""
# There are two families of related products
# AbstractProductA
class Pizza(object):
    def cook():
        pass
# ConcreteProductA1
class HawaiianPizza(Pizza):
    def cook(self):
        print("HawaiianPizza - ham & pineapple")
# ConcreteProductA2
class CheesePizza(Pizza):
    def cook(self):
        print("DeluxPizza - Cheddar & Mozzarella")
#AbstractProductB
class Chinese(object):
    def cook():
        pass
# ConcreteProductB1
class Dumplings(Chinese):
    def cook(self):
        print("Dumplings - ham & pineapple")
# ConcreteProductB2
class MoonCake(Chinese):
    def cook(self):
        print("MoonCake - sesame seeds, ground lotus seeds and duck eggs")
class Kiwi(object):
    def cook():
        pass
class LambRoast(Kiwi):
    def cook(self):
        print("Lamb - nicely burnt, drowned in gravey with 3 veg")
# ConcreteProductB2
class Pavlova(Chinese):
    def cook(self):
        print("crispy egg whites and lotsa cream")
class Chocolate(object):
    def cook():pass
class DarkChocolate(Chocolate):
    def cook(self):
        print("dark bitter and yummy")
class WhiteChocolate(Chocolate):
    def cook(self):
        print("white and yummy")

"""
The CLIENT code below currently has to make too many decisions
and know all about the food choices

Change things by applying the ABSTRACT FACTORY pattern
so the client only has to decide the type of feast
and does not need to know the details of feast preparation.

To make things simplier can you please ..
get rid of the constants (too much to remember)
get rid of the case statements (too difficult to maintain)

"""
CHINESE = 1
PIZZA = 2
KIWI = 3

class AbstractFactory(object):
    def makeMain(self):pass
    def makeDesert(self):pass
class ChineseFactory(AbstractFactory):
    def makeMain(self): return Dumplings()
    def makeDesert(self):return MoonCake()
class PizzaFactory(AbstractFactory):
    def makeMain(self): return CheesePizza()
    def makeDesert(self): return HawaiianPizza()
class KiwiFactory(AbstractFactory):
    def makeMain(self): return LambRoast()
    def makeDesert(self): return Pavlova()
class ChocolateFactory(AbstractFactory):
    def makeMain(self): return DarkChocolate()
    def makeDesert(self): return WhiteChocolate()
    
def feast(factory):
    print("Main")
    main = factory.makeMain()
    main.cook()
    print("Desert")
    desert = factory.makeDesert()
    desert.cook()
    
print("A Chinese feast")
feast( ChineseFactory() )
print("A Pizza feast")
feast( PizzaFactory() )
print("A Kiwi feast")
feast( KiwiFactory() )
print("A Chocolate feast")
feast( ChocolateFactory() )       