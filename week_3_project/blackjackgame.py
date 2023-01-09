import random

deck = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4, 14:4}

def get_card():
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
    
mycard1 = get_card()
mycard2 = get_card()
mycard3 = get_card()
mycard4 = get_card()

    
print(mycard1, mycard2, mycard3, mycard4, deck)
