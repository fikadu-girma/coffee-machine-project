menu = {
    "limu" : {
        "ingredient": {
            "water": 100,
            "coffee": 18,
        },
        "cost":45,  
    },
    "jimma" : {
        "ingredient": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost":55,
    },
    "wollega" : {
        "ingredient": {
            "water": 300,
            "milk": 100,
            "coffee": 24,
        },
        "cost":65,
    }
}


profit = 0

resources = {
    "water": 1000,
    "milk": 400, 
    "coffee": 300,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"sorry there is not enough {item}.")
           return False
    return True


def process_coins():
    print("Please insert the currency u have and insert 0 for none!(since we take a money by the following option and convert to ETB!).")
    total = 0
    total += float(input("how many dollar?: ")) * 145
    total += float(input("how many Yuan?: ")) * 18.35
    total += float(input("how many Dirham?: ")) * 35.77
    total += float(input("how many Yen?: ")) * 0.88
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"{change}ETB are remained.")
        global profit
        profit += drink_cost
        return True 
    else:
        print("Sorry that's not enough money. Money refunded!!!")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffee ☕️.")

is_on = True
while is_on:
    choice = input("which brand of Coffee u would like to drink? (limu/jimma/wollega) / write 'off' to close the machine and write 'report' to see the resource available.: \n")
    if choice == "off":
        print("The machine is CLOSED. Thank you for using!!!")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Accepted Money: {profit}ETB")
    else:
        if choice in menu:
            drink = menu[choice]
            if is_resource_sufficient(drink["ingredient"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredient"])
        else:
            print("Sorry, we don't serve that drink.")
