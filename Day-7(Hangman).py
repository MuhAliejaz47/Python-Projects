
      ###  Read_Me


##  Put the words of your choice into:

## word_list['']

## Make sure that you seperate every word by a comma and put it inside quatations.

## For example:

## word_list = ['banana', 'apple', 'mango']



import random

word_list = ['']

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

stages = -1
selected = random.choice(word_list)

the_word = ['_'] * len(selected)
end_of_game = False
print (the_word)

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in selected:
        for i in range(len(selected)):
            if selected[i] == guess:
                the_word[i] = guess
    else:
        stages = stages + 1
        print(HANGMANPICS[stages])


    print(' '.join(the_word))

    if stages == 6:
        print (f'You could not guess it! The word was {selected}')
        end_of_game == True
        break

    if '_' not in the_word:
        end_of_game = True
        print('Congratulations! You guessed the word.')
        print('The word was:', selected)
        break
