from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Indicates whether the machin is off or running
machine_off = False

# Object instance for Coffee Maker class
machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
menu_item = MenuItem

# While machine is not off....
while not machine_off:
    # Print all the options on the menu
    options = menu.get_items()
    # Ask customer what they want
    choice = input(f"What would you like? ({options}): ")

    # If answer is off, turn off coffee machine
    if choice == "off":
        machine_off = True
    
    # If answer is report, prints the current resources of the coffee machine
    elif choice == "report":
        machine.report()
        money.report()
    
    else:
        # If input is not on the menu, print error message, if yes, store drink in order_name
        drink = menu.find_drink(choice)
        # If current resource is enough to make the coffee, continue
        if machine.is_resource_sufficient(drink):
            cost = drink.cost
            # If payment is enough to pay the cost, continue
            if money.make_payment(cost):
                # Display the coffee being served
                machine.make_coffee(drink)
