DATA={
    "ESPRESSO":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":2,
    },
    "LATTE":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "cost":2.5,
    },
    "CAPPUCCINO":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100,
        },
        "cost":3,
    }
}

profit =0
resources = {
    "water":1000,
    "milk":1000,
    "coffee":1000,
}

def is_resources_sufficient(inputs):
    for item in inputs:
        if inputs[item] >= resources[item]:
            print(f'Sorry - not enough stock {item}')
    return True

def process_coin():
    total =int(input('how many quarters?'))*0.25
    total += int(input('how many dimes?'))*0.1
    total += int(input('how many nickles?')) *0.05
    total += int(input('how many pennies?')) *0.01
    return total

def is_transaction_ok(money_received,drink_cost):
    if money_received >= drink_cost:
        change =round(money_received-drink_cost,2)
        print(f'here is {change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('not enough money')
        return False

def get_coffer(name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"here is your name {name} coffe" )
    
on=True
while on:
    choice = input("what would you like :")
    if choice == 'off':
        on = False
    elif choice == 'report':
        print(f'water:{resources["water"]}ml')
        print(f'water:{resources["milk"]}ml')
        print(f'water:{resources["coffee"]}ml')
        print(f'profit-${profit}')
    else:
        drink = DATA[choice]
        if is_resources_sufficient(drink['ingredients']):
            pay = process_coin()
            if is_transaction_ok(pay,drink['cost']):
                get_coffer(choice,drink['ingredients'])