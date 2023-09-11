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

profit = 0 # 자판기 내부 돈의 양
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False if ingredients are insufficient'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def payment_process():
    '''Returns the total calculated from coins inserted.'''
    print("Please insert coins.")
    quarters = int(input("How many quarters? : ")) * 0.25
    dimes = int(input("How many dimes? : ")) * 0.1
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies? : ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_paid_successful(money_received, drink_cost):
    '''Return True when the payment is accepted, or False if money is inserted.'''
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2) 
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice] 
        if is_resource_sufficient(drink["ingredients"]):
            payment = payment_process()
            if is_paid_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])