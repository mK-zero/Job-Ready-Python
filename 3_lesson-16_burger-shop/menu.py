class food_item:
    """Represents a food item.
    A food item includes name and price."""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
    def get_price(self):
        return self.price

class burger(food_item):
    """A subclass based on food_item.
    Burger orders include name, price, and condiments."""
    def __init__(self, name, price):
        super(burger, self).__init__(name, price)
        self.condiments = []
    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)
    def __str__(self):
        s = super(burger, self).__str__()
        s = s + "Condiments: " + ", ".join(self.condiments)
        return s

class drink(food_item):
    """A subclass based on food_item.
    Drink orders include name, price, and size."""
    def __init__(self, name, size, price):
        super(drink, self).__init__(name, price)
        self.size = size
    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "oz"
        return s

class side(food_item):
    """A subclass based on food_item. 
    All side orders have the same price."""
    def __init__(self, name, price):
        super(side, self).__init__(name, price)

class combo(food_item):
    """An order that includes a name, price, multiple food items, and a discounted price based on the food items."""
    def __init__(self, name, b, d, s, discount):
        self.name = name
        self.burger = b
        self.drink = d
        self.side = s
        self.discount = discount
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount
    def __str__(self):
        s = ""
        s = s + "Combo: " + self.name + "\n"
        s = s + str(self.burger) + "\n" + str(self.drink) + "\n" + str(self.side) + "\n"
        s = s + "Combo Price Before Discount: $" + str(self.burger.get_price() + self.drink.get_price() + self.side.get_price()) + "\n"
        s = s + "Discount: $" + str(self.discount) + "\n"
        s = s + "Combo Price After Discount: $" + str(self.price) + "\n"

        return s