from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
my_menu = Menu()
my_coffemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffemaker.report()
        my_moneymachine.report()
    else:
        drink = my_menu.find_drink(choice)
        sufficiency = my_coffemaker.is_resource_sufficient(drink)
        if sufficiency is True:
            payment = my_moneymachine.make_payment(drink.cost)
            if payment is True:
                my_coffemaker.make_coffee(drink)
                my_coffemaker.report()
                my_moneymachine.report()



