#add
import os


def add(n1,n2):
    result_sum = n1 + n2
    return result_sum

def sub(n1,n2):
    result_sub = n1 - n2
    return result_sub

def mul(n1,n2):
    result_mul = n1 * n2
    return result_mul


def div(n1,n2):
    result_div = n1 / n2
    return result_div


operations ={ '+' : add,
             '-' : sub,
             '*' : mul,
             '/' : div,
}

def calculator():
    n1 = float(input('Enter a number: '))
    for symbol in operations:
        print(symbol)

    should_continue = True


    while should_continue:
        operator = input('Pick an operator: ')

        n2 = float(input('Enter a second number: '))

        calculation_function = operations[operator]
        answer = calculation_function(n1,n2)

        print(f'{n1} {operator} {n2} = {answer}')

        

        if input('DO you want to continue with last number? Type "y" for yes and "n" for no and setting up a new calculation: ') == 'y':
            n1 = answer
        else:
            should_continue = False
            calculator()
calculator()