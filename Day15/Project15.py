# Project 15

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")    

def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def total_coins():
    print("Please insert your coins.")
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.1
    total+=int(input("How many nickels?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total


def transaction_success(money_taken,cost_drink):
    if money_taken>=cost_drink:
        change=round(money_taken-cost_drink,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=cost_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    

print("Welcome to the Python Coffee Machine!")


machine_on=True
while machine_on:
    choice=input("What would you like? espresso / latte / cappuccino / off / report: ").lower() 
    if choice=="off":
        machine_on=False

    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}ml")
        print(f"money=${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=total_coins()
            if transaction_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





