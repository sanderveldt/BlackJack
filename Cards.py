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

def hit_or_stand():
    choice = qst.select(
        'Do you want to hit or stand?',
        choices = ['Hit', 'Stand']
    ).ask()
    return choice

class Deck:
    def __init__(self):
        self.deck = []
        for suit in card_suits:
            for value in card_values:
                self.deck.append(value + suit)
        self.deck *= 4

    def shuffle(self):
        rd.shuffle(self.deck)

    def deal_card(self):
        card = rd.choice(self.deck)
        self.deck.remove(card)
        return card

<<<<<<< HEAD

class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.value = 0
        self.aces = 0
      
    def add_card(self, card):
        self.hand.append(card)
        self.calculate_value()

    def calculate_value(self):
        self.value = 0
        self.aces = 0

        for card in self.hand:
            self.value += card_values[card[:-1]]
            if card[:-1] == 'A':
                self.aces += 1

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def display_hand(self):
        print(f"Your cards: {', '.join(self.hand)}")
        print(f"Hand value: {self.value}")
=======
## Add hand class
## add player Class (combine with hand class?) 
## Add dealer class
## Probably should put those in separate .py
>>>>>>> 2b5a26bf7b5dc2a71aa65b46116ea12bd1c04d3f


    





