### Blackjack Game in Pytho

import random as rd


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
    
    def __str__(self):
        return str(self.hand)

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

    def reset_hand(self):
        self.hand.clear()
        self.aces = 0
        self.value = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.hand = Hand([])
    
    def __str__(self):
        return f"{self.name}'s hand: {self.hand.hand}"
class Dealer:
    def __init__(self):
        self.hand = Hand([])

    def __str__(self):
        return f"Dealer's hand: {self.hand.hand}"
           
class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle()
        self.current_bet = 0
        self.rounds_played = 0
        self.player_wins = 0
        self.dealer_wins = 0


    def lay_bet(self):
        bet_options = [5, 10, 15, 20, 25, 50, 100, 150, 200, 250, 500]
        filtered_options = []
        for option in bet_options:
            if option <= self.player.balance:
                filtered_options.append(option)

        if self.player.balance > 0:
            filtered_options.append(self.player.balance)
            return filtered_options
        elif self.player.balance == 0:
            return "DEAD"
        
    def place_bet(self, amount):
        self.current_bet = amount
        self.player.balance -= amount    
   
    def first_deal(self):
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card()) 
            self.dealer.hand.add_card(self.deck.deal_card())

        if self.player.hand.value == 21:
            return "PLAYER_BLACKJACK"
        elif self.dealer.hand.value == 21:
            return "DEALER_BLACKJACK"
        else:            
            return "CONTINUE"
    
    def player_hit(self):
        self.player.hand.add_card(self.deck.deal_card())    
        if self.player.hand.value == 21:
            return "PLAYER_BLACKJACK"
        elif self.player.hand.value > 21:
            return "PLAYER_BUST"
        else:
            return "CONTINUE"
        
    def player_stand(self):
        return "PLAYER_STAND"
    
    def round_reset(self):
        self.rounds_played += 1
        self.player.hand.reset_hand()
        self.dealer.hand.reset_hand()
        self.reset_deck()
    
    def dealer_turn(self):
        while self.dealer.hand.value < 17:
            self.dealer.hand.add_card(self.deck.deal_card())
            if self.dealer.hand.value > 21:
                return "DEALER_BUST"
        return "DEALER_STAND"
    
    def check_winner(self):
        if self.player.hand.value > self.dealer.hand.value:
            return "PLAYER_WIN"
        elif self.player.hand.value < self.dealer.hand.value:
            return "DEALER_WIN"
        else:
            return "TIE"

    def payout(self, result):
        if result == "PLAYER_WIN":
            self.player.balance += self.current_bet * 2
            self.player_wins += 1
        elif result == "PLAYER_BLACKJACK":
            self.player.balance += self.current_bet * 2.5
            self.player_wins += 1
        elif result == "TIE":
            self.player.balance += self.current_bet
        else:
            self.dealer_wins += 1
        self.current_bet = 0
        
    
    def reset_deck(self):
        threshold = 52
        if len(self.deck.deck) < threshold:
            self.deck = Deck()
            self.deck.shuffle()

