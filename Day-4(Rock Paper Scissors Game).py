import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list = [rock, paper, scissors]

cchoice = random.randint(0,2)


hchoice = input ("Type 0 for Rock 1 for Paper and 2 for Scissors: ")


hchoice = int(hchoice)

hchoice = hchoice

print (list[hchoice])

print (list[cchoice])

if (cchoice - hchoice) == 1:
    print('You have lost the game!')

if (cchoice - hchoice) == 0:
    print('You drew the game!')

if (cchoice - hchoice) == -1:
    print('You have won the game!')


if (cchoice - hchoice) == -2:
    print('You have lost the game!')


if (cchoice - hchoice) == 2:
    print('You have won the game!')
