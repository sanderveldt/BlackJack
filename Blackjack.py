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
        card = self.deck.pop()
        return card


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.value = 0
        self.aces = 0

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

    def add_card(self, card):
        self.hand.append(card)
        self.calculate_value()

    def display_hand(self):
        print(f"Your cards: {', '.join(self.hand)}")
        print(f"Hand value: {self.value}")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand([])
        
class Dealer:
    def __init__(self):
        self.hand = Hand([])

class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle()
    
    def start_game(self):
        print("Welcome to Blackjack!")
        for x in range(2):
            self.player.hand.add_card(self.deck.deal_card()) 
        for x in range(2):
            self.dealer.hand.add_card(self.deck.deal_card()) 
        self.player.hand.display_hand()
    
    def hit_or_stand(self):
        choice = qst.select(
        'Do you want to hit or stand?',
        choices = ['Hit', 'Stand']).ask()
        return choice

    
player = Player(input("What is your name?: "))
dealer = Dealer()

deck = Deck()
deck.shuffle()

game1 = Game(player, dealer)

game1.start_game()  

game1.hit_or_stand()




