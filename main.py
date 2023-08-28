from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Indicates whether the machin is off or running
machine_off = False

# Object instance for Coffee Maker class
machine = CoffeeMaker()
money = MoneyMachine()

# While machine is not off....
while not machine_off:
    # Ask customer what they want
    choice = input("What would you like? (espresso/latte/cappuccino/): ")

    # If answer is off, turn off coffee machine
    if choice == "off":
        machine_off = True
    
    # If answer is report, prints the current resources of the coffee machine
    elif choice == "report":
        machine.report()
        money.report()
