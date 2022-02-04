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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 2. Check that resources are sufficient


def is_resource_sufficient(order_ingredients):
    """Returns true if resources are sufficient for the order, returns false otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}!")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please, insert coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Returns true if the transaction was successful, returns false otherwise"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Your change is {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money! Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True

# prompt the user each time the action is completed
while is_on:
    # prompt the user for the type of coffee they want to make
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("Goodbye!")
        # TODO: 1. Print report about machine
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # TODO: 3. Process coins
            payment = process_coins()
            # TODO: 4. Check that transaction is successful
            if is_transaction_successful(payment, drink["cost"]):
                # TODO: 5. Make the coffe and deduct the resources
                make_coffee(choice, drink["ingredients"])
