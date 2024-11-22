from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#create objects from the imported classes
maker = CoffeeMaker()
moneybank = MoneyMachine()

menulist = MenuItem("name", "water", "milk", "coffee", "cost")
menufunctions = Menu()
options = menufunctions.get_items()
# menuitems.name = "latte"
# print(menuitems)


coffee_active = True
while coffee_active == True:
    #ask the user what drink they'd like
    order_name = input(f"What would you like? {options} ")
    finddrink = menufunctions.find_drink(order_name)
    if order_name == "off":
        coffee_active = False
    elif order_name == "report":
        maker.report()
        moneybank.report()
    else:
        able_to_coffee = maker.is_resource_sufficient(drink = finddrink)
        #print(maker.is_resource_sufficient(drink = finddrink))
        if able_to_coffee:
            print("Let's gooo!")
            is_paid = moneybank.make_payment(cost=finddrink.cost)
            if is_paid:
                maker.make_coffee(order=finddrink)





        else:
            print(f"Sorry, there is not enough resources")
            makecoffee = False




