resources = {
    "water": 350,
    "milk": 250,
    "coffee": 200
}

machine_money = 0

MENU = {
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 2.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 3.5
    },
    "americano": {
        "ingredients": {
            "water": 300,
            "milk": 0,
            "coffee": 20
        },
        "cost": 2.5
    }
}

ACTIONS = ["capuccino", "espresso", "latte", "americano", "off", "report"]

def use_current_resources(request: str):
    usage = MENU[request]["ingredients"]

    for ingredient, use in zip(resources.keys(), usage.values()):
        resources[ingredient] -= use


def prepare_beverage(request: str):
    are_enough_resources = check_resources(request)

    if not are_enough_resources:
        return

    money_input = process_coins()

    if money_input < MENU[request]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        global  machine_money
        machine_money += MENU[request]["cost"]

        use_current_resources(request)


        if money_input > MENU[request]["cost"]:
            exchange = money_input - MENU[request]["cost"]
            print(f"Here is {exchange:.2f} {'cents' if exchange < 1 else 'dollars'} in change")


def process_coins():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def check_resources(beverage_type: str) -> bool:
    enough_resources = True
    # [water, milk, coffee]
    resources_keys = list(resources.keys())

    current_resources = list(resources.values())
    item_uses = list(MENU[beverage_type]["ingredients"].values())

    for i in range(0, len(resources)):
        if current_resources[i] < item_uses[i]:
            enough_resources = False
            print(f"Sorry there is not enough {resources_keys[i]}.")

    return enough_resources

def print_report():
    print("Current report of resources and money")
    for index, (k, v) in enumerate(resources.items()):
        print(f"{k}: {v}{'g' if k == "coffee" else 'ml'}")
    print(f"Money: {machine_money}")

def request_input() -> str:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    while request not in ACTIONS:
        print("Invalid input, please try again")
        request = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    return request


if __name__ == '__main__':
    while True:
        user_request = request_input()

        if user_request == 'report':
            print_report()

        elif user_request == 'off':
            break
        else:
            prepare_beverage(user_request)


