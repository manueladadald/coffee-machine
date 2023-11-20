from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

coffee_on = True
while coffee_on:
    options = menu.get_items()
    coffee_choice = input(f"\nWhat would you like? ({options}): ").lower()
    if coffee_choice == "off":
        coffee_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
