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

    def display_dealer_hand(self):
            print(f"Dealer's cards: {', '.join(self.hand)}")
            print(f"Dealer's hand value: {self.value}")

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
        print("The first two cards are dealt.")
        for x in range(2):
            self.player.hand.add_card(self.deck.deal_card()) 
        for x in range(2):
            self.dealer.hand.add_card(self.deck.deal_card()) 
        self.player.hand.display_hand()
        print(f"Dealer's first card: {self.dealer.hand.hand[0]}")
        if self.player.hand.value == 21:
            return "PLAYER_BLACKJACK"
        elif self.dealer.hand.value == 21:
            return "DEALER_BLACKJACK"
        else:            
            return "CONTINUE"
    
    def hit_or_stand(self):
        choice = qst.select(
        'Do you want to hit or stand?',
        choices = ['Hit', 'Stand']).ask()
        return choice
    
    def player_turn(self):
        while True:
            choice = self.hit_or_stand()
            if choice == 'Hit':
                self.player.hand.add_card(self.deck.deal_card())
                self.player.hand.display_hand()
                if self.player.hand.value > 21:
                    print("You're dead!The House wins!")
                    return "BUST"
            else:
                print("You stand. Dealer's turn.")
                return "STAND"
    
    def dealer_turn(self):
        print(f"Dealer's cards: {', '.join(self.dealer.hand.hand)}")
        print(f"Dealer's hand value: {self.dealer.hand.value}")
        while self.dealer.hand.value < 17:
            print("Dealer hits.")
            self.dealer.hand.add_card(self.deck.deal_card())
            self.dealer.hand.display_dealer_hand()
            if self.dealer.hand.value > 21:
                print("Dealer's dead! You win!")
                return "BUST"
            elif self.dealer.hand.value >= 17:
                print("Dealer stands.")
                return "STAND"
        return "STAND"

    def play_round(self):

    
player = Player(input("What is your name?: "))
dealer = Dealer()

deck = Deck()
deck.shuffle()

game1 = Game(player, dealer)

game1.start_game() 
if game1.player_turn():
    if game1.dealer_turn():
        if game1.player.hand.value > game1.dealer.hand.value:
            print("You win!")
        elif game1.player.hand.value < game1.dealer.hand.value:
            print("The House wins!")
        else:
            print("It's a tie!") 
