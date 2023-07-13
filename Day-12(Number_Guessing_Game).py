
import random

number = random.randrange(1,101)


print('Welcome to the Number Guessing Game!')
print('I am Thinking of a Number Between 1 -100')
decision = input('Choose a Difficulty. Type "easy" or "hard": ')


def easy():

    print('You have 10 attempts remaining to guess the number.')
    attempts = 10

    for i in range(attempts): 

        guess = int(input('Make a guess: '))

        if guess == number:
            print(f'You win the number was {guess}')
            return guess
        
        elif guess > number:
            print('Too high')
            print(f'You have {attempts -1} attempts remaining')
            attempts = attempts -1

        elif attempts == 0:
            print(f'You lost the number was {number}')

        else:
            print(f'You have {attempts -1} attempts remaining')
            attempts = attempts -1
            print('Too low')


def hard():

    print('You have 5 attempts remaining to guess the number.')
    attempts = 5

    for i in range(attempts): 
        guess = int(input('Make a guess: '))
        
        if guess == number:
            print(f'You win the number was {guess}')
            return guess
        
        elif guess > number:
            print(f'You have {attempts -1} attempts remaining')
            attempts = attempts -1
            print('Too high')

        else:
            print(f'You have {attempts -1} attempts remaining')
            attempts = attempts -1
            print('Too low')


if decision == 'easy':

    easy()

if decision == 'hard':

    hard()

if decision != 'easy' and decision != 'hard': 
    print('Enter a Valid Command')

print(f'The number was {number}')


