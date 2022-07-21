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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

required_drink = ""
profit = 0


def print_report():
    for res in resources:
        print(f"{res}: {resources[res]}")
    print(f"money: {profit}")


def check_resources():
    ingredients = MENU[required_drink]["ingredients"]
    for res, val in ingredients.items():
        if val > resources[res]:
            print("Sorry there is not enough", res)
            return False
    return True


def proc_coins():
    """Returns the total money iserted by the user"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(payment):
    """Return True if the transaction is accepted and false otherwise"""
    drink_cost = MENU[required_drink]["cost"]
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee():
    for ing in MENU[required_drink]["ingredients"]:
        resources[ing] -= MENU[required_drink]["ingredients"][ing]


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino)")
    if user_input == "off":
        break
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        required_drink = user_input
        if check_resources():
            payment = proc_coins()
            if is_transaction_successful(payment):
                make_coffee()
    else:
        print("Sorry. Invalid input")
