from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
coffe_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f'What would u like? {options}: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        sufficient = coffe_maker.is_resource_sufficient(drink)
        if sufficient == True:
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
        else:
            print(f'{drink} is not available')
