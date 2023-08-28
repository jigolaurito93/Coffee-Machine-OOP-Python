from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_off = False

coffee_maker = CoffeeMaker()

while not machine_off:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")

    if choice == "off":
        machine_off = True
