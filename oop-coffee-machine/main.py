from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True


while is_on:
    options = menu.get_items()
    # Prompt User
    choice = input(f"What would type of drink would you like? {options}):")
    # Turn off machine with 'off' input
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Print Report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # Check resources are sufficient
        # Check transaction was successful
        # Process coins
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make Coffee
            coffee_maker.make_coffee(drink)
