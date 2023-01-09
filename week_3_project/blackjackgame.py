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
    
def play_blackjack():
    fresh_deck = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4, 14:4}
    deck = dict(fresh_deck)
    player_value = 0
    cpu_value = 0
    
    player_cards = [get_card(deck), get_card(deck)]
    cpu_cards = [get_card(deck), get_card(deck)]
    player_value = get_value(player_cards)
    cpu_value = get_value(cpu_cards)
    
    
    
    print(player_cards, cpu_cards, player_value, cpu_value)
    
play_blackjack()