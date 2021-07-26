"""
HAS  ABSTRACT FACTORY
"""
# There ar
e two families of related products
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
class Dumplings(Pizza):
    def cook(self):
        print("Dumplings - ham & pineapple")
# ConcreteProductB2
class MoonCake(Pizza):
    def cook(self):
        print("MoonCake - sesame seeds, ground lotus seeds and duck eggs")


class AbstractFactory(object): #1
    def createMain(self): #2
        return null
    def createDesert(self): #3
        return null
class PizzaFactory(AbstractFactory): #4 
    def createMain(self): #5
        return CheesePizza()
    def createDesert(self): #6
        return HawaiianPizza()
class ChineseFactory(AbstractFactory): #4 
    def createMain(self): #5
        return Dumplings()
    def createDesert(self): #6
        return MoonCake()

def feast(factory): #7
    print("Main")
    main = factory.createMain() #8
    main.cook()
    print("Desert")
    desert = factory.createDesert() #9
    desert.cook()    
"""
The CLIENT code below  only has to decide the type of feast
and does not need to know the details of feast preparation
"""

    
print("A Chinese feast")
feast(ChineseFactory()) #10 
print("A Pizza feast")
feast(PizzaFactory()) #10
        