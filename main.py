
"""
This project will simulate a coffee vending machine. Here are the steps:
-Prompt user. if take order. print report or turn off
-check if enough ingredients. if no reset loop, if yes move to next step.
-check for proper amount of money. if no, refund money and reset. if yes, refund change and proceed to next step
-make coffee --> reduce resources, add to profit, and print here is your latte
-ask again what to order

5 responses to input: 3 options, and 1 report, off
there's 4 things that can make a turn repeat: not enough money, not enough ingredients, report, successful order

# in future versions I'll have the thing power off, or refuse to display coffeee if it's out of ingredients for that one
"""


import sys

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

money = 0
order = ""
on = True


def display_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")


def check_resources(drink_name):
    ingredients_needed = MENU[drink_name]["ingredients"]

    for ingredient, required_amount in ingredients_needed.items():
        if resources.get(ingredient, 0) < required_amount:
            return False, ingredient

    return True, None #we leave this return outside of the for loop because it was ending the for loop/function too early by immedaitely
                #doing the return statement if one of the other ingredients had sufficient amounts of resources. I had that bug earlier.



def take_payment():
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickels = int(input("how many nickels?: "))
    num_pennies = int(input("how many pennies?: "))
    q = .25
    d = .1
    n = .05
    p = .01
    payment_amount = (num_quarters * q) + (num_dimes * d) + (num_nickels * n) + (num_pennies * p)
    return payment_amount

def return_change(paid_amount, item_cost):
    change = paid_amount - item_cost
    if paid_amount > item_cost:
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        return change
    else:
        return None


def make_coffee(drink_name):  # this makes the coffee and thus uses some of the resources
    ingredients_needed = MENU[drink_name]["ingredients"]
    for ingredient, amount in ingredients_needed.items():
        if ingredient in resources:
            if resources[ingredient] >= amount:
                resources[ingredient] -= amount


while on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        sys.exit()
    elif order == "report":
        display_report()
    elif order in MENU:
        enough_resources, missing_resource = check_resources(order)
        if enough_resources == False:
            print(f"Not enough {missing_resource}")
        elif True:
            paid_amount = take_payment()
            if paid_amount < MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                return_change(paid_amount, MENU[order]["cost"])
                make_coffee(order)
                money += MENU[order]["cost"]
    else:
        print("That's not a valid option. Please try again")
