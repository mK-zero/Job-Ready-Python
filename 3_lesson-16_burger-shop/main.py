from menu import burger
from menu import drink
from menu import side
from menu import combo
from order import order

BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese"]

DRINK_TYPES = ["fanta", "coca cola", "sprite"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00]

SIDE_PRICE = 3.00
SIDES = ["fries", "coleslaw", "salad"]

COMBO_DISCOUNT = 2.00

def get_burger_order():
    """Asks the user for their burgers.
    Returns a burger with any amount of condiments."""
    b = burger("Burger", BURGER_PRICE)
    q1 = input("Do you want any condiments on your burger? (y for yes) ")
    if q1.lower() == "y":
        for condiment in BURGER_CONDIMENTS:
            q = input("Do you want " + str(condiment) + "? (y/n): ")
            if q.lower() == "y":
                b.add_condiment(condiment)
    return b

def get_drink_order():
    """Asks the user for their drinks.
    Returns a valid drink choice and size."""
    print("These are the available drinks: ")
    print(DRINK_TYPES)
    print("These are the available sizes: ")
    print(DRINK_SIZES)
    choice = False
    drink_name = None
    drink_size = None
    drink_price = None
    while choice == False:
        q1 = input("What drink do you want? ")
        if q1.lower() in DRINK_TYPES:
            choice = True
            drink_name = q1.lower()
        else:
            print("Please enter a valid drink.")
            print(DRINK_TYPES)
    choice = False
    while choice == False:
        q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
        if q1 in str(DRINK_SIZES):
            choice = True
            drink_size = int(q1)
        else:
            print("Please enter a valid size.")
    # locate the price of the drink based on the index of the size:
    drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)]
    d = drink(drink_name, drink_size, drink_price)
    return d

def get_side_order():
    """Asks the user for their sides.
    Returns the valid side choices."""
    print("These are the available sides: ")
    print(SIDES)
    choice = False
    side_name = None
    while choice == False:
        q1 = input("What side do you want? ")
        if q1.lower() in SIDES:
            choice = True
            side_name = q1.lower()
        else:
            print("Please enter a valid side.")
            print(SIDES)
    s = side(side_name, SIDE_PRICE)
    return s

def get_combo_order():
    """Gets the burger, drink, and side for the combo order."""
    print("Let's get you a combo meal!")
    
    print("First, let's order the burger for your combo.")
    b = get_burger_order()
    
    print("Now, let's order the drink for your combo.")
    d = get_drink_order()
    
    print("Finally, let's order the side for your combo.")
    s = get_side_order()

    c = combo("Combo", b, d, s, COMBO_DISCOUNT)
    #print(str(c))
    return c

def order_once():
    """Print and ask the user for their order choice."""
    possible_options = [1, 2, 3, 4]
    choice = None
    while choice == None:
        print("Type 1 for a Burger.")
        print("Type 2 for a Drink.")
        print("Type 3 for a Side.")
        print("Type 4 for a Combo.")
        q1 = input("Please enter your choice: ")
        if q1 in str(possible_options):
            choice = int(q1)
        else:
            continue
    item = None
    if choice == 1:
        item = get_burger_order()
    elif choice == 2:
        item = get_drink_order()
    elif choice == 3:
        item = get_side_order()
    elif choice == 4:
        item = get_combo_order()
    return item

def order_many():
    """Ask the user for their order."""
    print("Welcome to Mary's Burger Shop!")
    q1 = input("May I have your name for the order? ")
    o = order(q1)
    print("Let's get your order in!")
    done = False
    while done == False:
        item = order_once()
        o.add_item(item)
        q1 = input("Do you need more items? (Enter n to stop.) ")
        if q1.lower()=="n":
            done = True
    return o

client_order = order_many()
client_order.display()