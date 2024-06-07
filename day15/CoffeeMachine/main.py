MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money_current = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 2.check resources sufficient
# What would you like? (espresso/latte/cappuccino): espresso
# Sorry there is not enough water.

def is_resource_sufficient(order_ingredient):
    """return True if order can be made, False if ingredient are insufficient"""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """return True when payment is accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global money_current
        money_current += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredient from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# TODO 1.print report
machine_shutdown = False

while not machine_shutdown:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_current}")
    elif order == "off":
        machine_shutdown = True
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])







# TODO 3.process coins
# Please insert coins.
# how many quarters?: 10
# how many dimes?: 10
# how many nickles?: 0
# how many pennies?: 0
# TODO 4.check transaction successful
# Sorry that's not enough money. Money refunded.
# Here is $2.0 in change.
# TODO 5.make coffee
# Here is your espresso ☕️. Enjoy!
