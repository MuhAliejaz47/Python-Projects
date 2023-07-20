import random
import game_data

score = 0
game_over = False

def Comparison_Generator():
    selected_dict = random.sample(game_data.data, 2)  # Select 2 unique dictionaries from the 'data' list

    name1 = selected_dict[0]['name']
    name2 = selected_dict[1]['name']

    des1 = selected_dict[0]['description']
    des2 = selected_dict[1]['description']

    country1 = selected_dict[0]['country']
    country2 = selected_dict[1]['country']

    print(f'Compare A: {name1}, a {des1} from {country1}')
    print()
    print(f'Against B: {name2}, a {des2} from {country2}')
    print()

    return selected_dict

while not game_over:
    selected_dict = Comparison_Generator()

    followers1 = selected_dict[0]['follower_count']
    followers2 = selected_dict[1]['follower_count']

    if followers1 == followers2:
        correct_answer = 'A' or 'B'

    elif followers1 > followers2:
        correct_answer = 'A'

    else:
        correct_answer = 'B'

    answer = input('Who has more followers? Type "A" or "B": ').upper()
    print()

    if answer == correct_answer:
        print('You are right!')
        print()
        print(f'Your Current score is {score + 1}')
        print()
        score += 1
    else:
        print("Sorry that's wrong")
        print()
        print(f'Your Final Score is: {score}')
        print()
        game_over = True
