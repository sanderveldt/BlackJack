### Blackjack Game in Python ###

import random as rd
import questionary as qst

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

hand = []
def deal_card():
    card = rd.choice(deck)
    hand.append(card)
    deck.remove(card)

def hit_or_stand():
    choice = qst.select(
        'Do you want to hit or stand?',
        choices = ['Hit', 'Stand']
    ).ask()
    return choice

deal_card()
deal_card()

hit_or_stand()

print(hand) 




    





