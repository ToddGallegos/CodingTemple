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
    
def play_blackjack():
    deck = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4, 14:4}
    shadow_deck = deck
    player_value = 0
    cpu_value = 0
    
    player_cards = [get_card(deck), get_card(deck)]
    cpu_cards = [get_card(deck), get_card(deck)]
    
    for card in player_cards:
        if card < 11:
            deck[card] -= 1
        elif card == "J":
            deck[11] -= 1
        elif card == "Q":
            deck[12] -= 1
        elif card == "K":
            deck[13] -= 1
        elif card == "A":
            deck[14] -= 1
            
    for card in cpu_cards:
        if card < 11:
            deck[card] -= 1
        elif card == "J":
            deck[11] -= 1
        elif card == "Q":
            deck[12] -= 1
        elif card == "K":
            deck[13] -= 1
        elif card == "A":
            deck[14] -= 1
    
    print(player_cards, cpu_cards)
    
play_blackjack()