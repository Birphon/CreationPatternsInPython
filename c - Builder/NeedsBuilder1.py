"""
TASK:   (1) redesign this system so it uses the Builder GOF pattern
        (2) add the additional Hawaiian Pizza option mentioned at the end
"""
class PizzaKitMatic:
    def __init__(self, type):
        self.type = type
        self.ingedients = []
    def makePizza(self):
        """This design is inflexible.
            The case statement in this method
            will forever have to be edited and extended
            as new types of pizzas are added to the range.
        """
        self.ingedients.append('Soft Crust Base')
        # add main topping
        if self.type == 'Veggie':
            self.ingedients.append('Mushrooms')
        elif self.type == 'Chicken':
            self.ingedients.append('Chicken')
        # add cheese
        if self.type == 'Veggie':
            self.ingedients.append('Moz')
        elif self.type == 'Chicken':
            self.ingedients.append('Blue Cheese')
        # add additional topping
        if self.type == 'Veggie':
            self.ingedients.append('Sun Dried Tomatoes & Olives')
        elif self.type == 'Chicken':
            self.ingedients.append('Capsicums')
        return self.ingedients

if __name__ == "__main__":
    chickenPizzaMachine = PizzaKitMatic('Chicken')
    print(chickenPizzaMachine.makePizza())
    #['Soft Crust Base', 'Mushrooms', 'Moz', 'Sun Dried Tomatoes & Olives']

    veggiePizzaMachine = PizzaKitMatic('Veggie')
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