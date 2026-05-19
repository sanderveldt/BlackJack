### Blackjack Game in Python ###

import random as rdm

card_values = { 
    'A' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

card_suits = [ '♠', '♥', '♦', '♣' ]


deck = []
for suit in card_suits:
    for value in card_values:
        deck.append(value + suit)
    deck *= 4

rdm.shuffle(deck) 

print(deck)

      





