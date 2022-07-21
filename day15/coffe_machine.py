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


def print_report():
    for res, val in resources.items():
        print(res, "\b:", val)


def check_resources():
    ingredients = MENU[required_drink]["ingredients"]
    for res, val in ingredients.items():
        if val > resources[res]:
            print("Sorry there is not enough", res)
            return False
    return True


def proc_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < MENU[required_drink]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return False
    global profit
    profit += total

def is_transaction_successful(payment, MENU[required_drink]["cost"]):




required_drink = ""
profit = 0


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

        else:
            break
