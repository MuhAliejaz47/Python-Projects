import os


final_bid_list = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


name = input('What is your name? ')
bid = int(input('What are you willing to bid? '))

bidding_dictionary = {
    'name': name,
    'bid': bid,
}

final_bid_list.append(bidding_dictionary)

direction = input('Are there any more bidders? Type "n" for no and "y" for yes: ')


def function(name, bid, direction):
    clear_screen()
    name = input('What is your name? ')
    bid = int(input('What are you willing to bid? '))

    bidding_dictionary = {
        'name': name,
        'bid': bid,
    }
    final_bid_list.append(bidding_dictionary)

    direction = input('Are there any more bidders? Type "n" for no and "y" for yes: ')
    if direction == 'y':
        function(name, bid, direction)
    if direction == 'n':
        determine_winner()


def determine_winner():
    clear_screen()
    if len(final_bid_list) == 1:
        winner = final_bid_list[0]
    else:
        highest_bid = 0
        winner = None
        for bidder in final_bid_list:
            if bidder['bid'] > highest_bid:
                highest_bid = bidder['bid']
                winner = bidder

    print(f'The winner is {winner["name"]} with a bid of {winner["bid"]}')


if direction == 'y':
    function(name, bid, direction)
if direction == 'n':
    determine_winner()
