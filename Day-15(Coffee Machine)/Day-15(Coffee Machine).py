from data import resources
from data import MENU

over = False
money = 0

def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money:.2f}')

def check_resources(coffee_type):
    water_used = int(MENU[coffee_type]['ingredients']['water'])
    milk_used = int(MENU[coffee_type]['ingredients'].get('milk', 0))  # Get milk if available, default to 0
    coffee_used = int(MENU[coffee_type]['ingredients']['coffee'])

    if resources['water'] < water_used:
        print('Sorry, there is not enough water.')
        return False
    elif resources['milk'] < milk_used:
        print('Sorry, there is not enough milk.')
        return False
    elif resources['coffee'] < coffee_used:
        print('Sorry, there is not enough coffee.')
        return False

    return True

def make_coffee(cost):
    print('Please insert coins.')
    quarters = int(input('How many quarters: '))
    nickels = int(input('How many nickels: '))
    dimes = int(input('How many dimes: '))
    pennies = int(input('How many pennies: '))

    money_inserted = quarters * 0.25 + nickels * 0.05 + dimes * 0.1 + pennies * 0.01
    change = money_inserted - cost

    if change < 0:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False
    elif change >= 0:
        print(f'Here is ${change:.2f} in change.')
        return True
    else:
        return True

while not over:
    decision = input('What would you like to have? (report/espresso/latte/cappuccino/exit): ')

    if decision == 'report':
        report()

    elif decision == 'espresso':
        if 'espresso' in MENU and check_resources('espresso') and make_coffee(MENU['espresso']['cost']):
            resources['water'] -= int(MENU['espresso']['ingredients']['water'])
            resources['coffee'] -= int(MENU['espresso']['ingredients']['coffee'])
            money += MENU['espresso']['cost']

    elif decision == 'latte':
        if 'latte' in MENU and check_resources('latte') and make_coffee(MENU['latte']['cost']):
            resources['water'] -= int(MENU['latte']['ingredients']['water'])
            resources['milk'] -= int(MENU['latte']['ingredients']['milk'])
            resources['coffee'] -= int(MENU['latte']['ingredients']['coffee'])
            money += MENU['latte']['cost']

    elif decision == 'cappuccino':
        if 'cappuccino' in MENU and check_resources('cappuccino') and make_coffee(MENU['cappuccino']['cost']):
            resources['water'] -= int(MENU['cappuccino']['ingredients']['water'])
            resources['milk'] -= int(MENU['cappuccino']['ingredients']['milk'])
            resources['coffee'] -= int(MENU['cappuccino']['ingredients']['coffee'])
            money += MENU['cappuccino']['cost']

    elif decision == 'exit':
        over = True
    else:
        print('Invalid input. Please try again.')
