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

# # TODO: 1. print report.✅
# # TODO: 2. check resources sufficient✅
# # TODO: 3. process coins.✅
# # TODO: 4. check transaction successful.✅
# # TODO: 5. Make coffee✅


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0



def check_resources(user_input):
    """check to know if available resources are enough to make user's request"""
    if user_input == "espresso":
        if water < 50:
            return "sorry there is no enough water"
        elif coffee < 18:
            return "sorry there is no enough coffee"
        else:
            return "Please insert coin"
    elif user_input == "latte":
        if water < 200:
            return "sorry there is no enough water"
        elif coffee < 24:
            return "sorry there is no enough coffee"
        elif milk < 150:
            return "sorry there is no enough milk"
        else:
            return "Please insert coin"
    elif user_input == "cappuccino":
        if water < 250:
            return "sorry there is no enough water"
        elif coffee < 24:
            return "sorry there is no enough coffee"
        elif milk < 100:
            return "sorry there is no enough milk"
        else:
            return "Please insert coin"


def process_coin():
    """check and process payment"""
    quarter = int(input("How many quarters? "))
    quarter *= 0.25
    dimes = int(input("How many dimes? "))
    dimes *= 0.10
    nickles = int(input("How many nickles? "))
    nickles *= 0.05
    pennies = int(input("How many pennies? "))
    pennies *= 0.01
    cost = MENU[user_input]["cost"]
    money = round(quarter + dimes + nickles + pennies, 2)
    change = money - cost
    print(f"${money}")
    if money > cost:
        return f"Here is ${change} in change. \nHere is your {user_input}☕️ Enjoy!"
    else:
        return "Sorry, not enough money. Money refunded."


is_now = True
while is_now:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_now = False
    elif user_input == "report":
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}ml \nMoney: {money}$")
    else:
        print(check_resources(user_input))
        print(process_coin())
        water = resources["water"] - MENU[user_input]["ingredients"]["water"]
        coffee = resources["milk"] - MENU[user_input]["ingredients"]["coffee"]
        milk = resources["coffee"] - MENU[user_input]["ingredients"]["milk"]
