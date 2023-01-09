import random

def get_card(deck):
    num1 = random.randint(2, 14)
    if num1 < 11 and deck[num1] > 0:
        mycard = num1
        deck[num1] -= 1
    elif num1 == 11 and deck[num1] > 0:
        mycard = "J"
        deck[num1] -= 1
    elif num1 == 12 and deck[num1] > 0:
        mycard = "Q"
        deck[num1] -= 1
    elif num1 == 13 and deck[num1] > 0:
        mycard = "K"
        deck[num1] -= 1
    elif num1 == 14 and deck[num1] > 0:
        mycard = "A"
        deck[num1] -= 1
    else:
        mycard = get_card()
    return mycard

def get_value(hand):
    value = 0
    for card in hand:
        if type(card) == int:
            value += card
        elif type(card) == str and card != "A":
            value += 10
        elif card == "A":
            value += 11
    return value

def clscr():
    print("\n"*50)
    
def play_blackjack():
    fresh_deck = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4, 14:4}
    deck = dict(fresh_deck)
    player_value = 0
    cpu_value = 0
    
    clscr()
    choice = input("Welcome to BlackJack! Press ENTER to play. Type 'rules' to read the rules. Type 'quit' to quit.\n")
    if choice == "rules":
        print("Object of the Game:\nEach participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.")
        print("Card Values/scoring:\nAn ace is worth 1 or 11. Face cards are 10 and any other card is its own value.")
        print("How to Play:\nThe Player and the Dealer are both dealt 2 cards. One of the dealer's cards remains hidden. You may continue taking more cards as many times as you like. The dealer will take cards until their score is over 16.")
    
    player_cards = [get_card(deck), get_card(deck)]
    cpu_cards = [get_card(deck), get_card(deck)]
    player_value = get_value(player_cards)
    cpu_value = get_value(cpu_cards)
    hit = 'y'
    cpu_hit = 'y'
    
    while hit == 'y':
        clscr()
        print(f"YOUR CARDS: {' '.join(map(str, player_cards))}\nDEALER'S CARDS: {cpu_cards[0]} ?\n")
        hit = input("Do you want another card?\n'y' or 'n': ")
        if hit == 'y':
            player_cards.append(get_card(deck))
            player_value = get_value(player_cards)
        if player_value > 21:
            play_again = input("You busted! Play again?\n'y' or 'n': ")
    while cpu_hit == 'y':
        clscr()
        print(f"YOUR CARDS: {' '.join(map(str, player_cards))}\nDEALER'S CARDS: {' '.join(map(str, cpu_cards))}\n")
        print("Dealer hits.")
        cpu_cards.append(get_card(deck))
        cpu_value = get_value(cpu_cards)
    if cpu_value > 21:
        play_again = input("The dealer busted! Play again?\n'y' or 'n': ")
    if player_value > cpu_value and player_value < 22:
        play_again = input("YOU WIN!!! Play again?\n'y' or 'n': ")
    elif cpu_value > player_value and cpu_value < 22:
        play_again = input("You lost. Play again?\n'y' or 'n': ")
    else:
        play_again = input("It's a tie. Play again?\n'y' or 'n': ")
    
    
play_blackjack()