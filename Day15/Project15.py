MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"  ❌ Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted with input validation."""
    print("Please insert coins.")
    try:
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total
    except ValueError:
        print("  ⚠️ Invalid input. Please enter numbers only. Refunded.")
        return 0

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"  💰 Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("  ❌ Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"  ☕ Here is your {drink_name} ☕. Enjoy!")

# --- MAIN PROGRAM LOOP ---
is_on = True
print("--- Welcome to the Professional Coffee Machine ---")

while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"  💧 Water: {resources['water']}ml")
        print(f"  🥛 Milk: {resources['milk']}ml")
        print(f"  ☕ Coffee: {resources['coffee']}g")
        print(f"  💵 Profit: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment > 0 and is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("  ⚠️ Invalid selection. Please choose from the menu.")