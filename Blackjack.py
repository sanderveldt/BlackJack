### Blackjack Game in Pytho

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

    def display_hand(self, current_bet):
        print(f"Your cards: {', '.join(self.hand)}")
        print(f"Hand value: {self.value}")
        if current_bet > 0:
            print(f"Current bet: {current_bet}")
        else:
            return
        

    def display_dealer_hand(self):
            print(f"Dealer's cards: {', '.join(self.hand)}")
            print(f"Dealer's hand value: {self.value}")

    def reset_hand(self):
        self.hand.clear()
        self.aces = 0
        self.value = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 0
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
        self.current_bet = 0
        self.rounds_played = 0
        self.player_wins = 0
        self.dealer_wins = 0


    def lay_bet(self):
        print(f"Your current balance: {self.player.balance}")
        bet_options = [5, 10, 15, 20, 25, 50, 100]
        filtered_options = []
        for option in bet_options:
            if option <= self.player.balance:
                filtered_options.append(qst.Choice(f"${option}", value = option))

        if self.player.balance > 0:
            filtered_options.append(qst.Choice(f"ALL-IN (${self.player.balance})", value = self.player.balance))
        else:
            print("You're out of money!")
            return 

        bet = qst.select(
            'How much do you want to bet?',
            choices = filtered_options).ask()
        
        self.current_bet = bet
        self.player.balance -= bet
    
    def payout(self, result):
        if result == "PLAYER_WIN":
            self.player.balance += self.current_bet * 2
            self.player_wins += 1
        elif result == "DEALER WIN":
            self.dealer_wins += 1
        elif result == "TIE":
            self.player.balance += self.current_bet
   
    def first_deal(self):
        print("The first two cards are dealt.")
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card()) 
            self.dealer.hand.add_card(self.deck.deal_card())

        self.player.hand.display_hand(self.current_bet)
        print(f"Dealer's first card: {self.dealer.hand.hand[0]}")

        if self.player.hand.value == 21 :
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
            if self.player.hand.value == 21:
                    return "BLACKJACK"
            elif self.player.hand.value > 21:
                    return "BUST"

            choice = self.hit_or_stand()

            if choice == 'Hit':
                self.player.hand.add_card(self.deck.deal_card())
                self.player.hand.display_hand(self.current_bet)
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
                return "BUST"
            elif self.dealer.hand.value >= 17:
                print("Dealer stands.")
                return "STAND"
        return "STAND"
    
    def check_winner(self):
        if self.player.hand.value > self.dealer.hand.value:
            print("You win!")
            return "PLAYER_WIN"
        elif self.player.hand.value < self.dealer.hand.value:
            print("The House wins!")
            return "DEALER_WIN"
        else:
            print("It's a tie!")
            return "TIE"

    def play_game(self):
        self.lay_bet()
        first_turn = self.first_deal()
        if first_turn == "PLAYER_BLACKJACK":
            print("Congratulations! You got Blackjack! You win!")
            self.player_wins += 1
            self.player.balance += self.current_bet * 2
            return
        elif first_turn == "DEALER_BLACKJACK":
            print("Dealer got Blackjack! The House wins!")
            self.dealer_wins += 1
            return 
        elif first_turn == "CONTINUE":
            
            player_status = self.player_turn()
            if player_status == "BLACKJACK":
                print("Congratulations! You got Blackjack! You win!")
                self.player_wins += 1
                self.player.balance += self.current_bet * 2
                return
            elif player_status == "BUST":
                print("You're dead! The House wins!")
                self.dealer_wins += 1
                return
            elif player_status == "STAND":
                dealer_status = self.dealer_turn()
                if dealer_status == "BUST":
                    print("Dealer's dead! You win!")
                    self.player_wins += 1
                    self.player.balance += self.current_bet * 2
                    return
                elif dealer_status == "STAND":
                    result = self.check_winner()
                    self.payout(result)
        return 
    
    def reset_deck(self):
        threshold = 52
        if len(self.deck.deck) < threshold:
            print("The dealer shuffles a new deck.")
            self.deck = Deck()
            self.deck.shuffle()

    def game_loop(self):
        while True:
            self.reset_deck()
            self.player.hand.reset_hand()
            self.dealer.hand.reset_hand()
            self.current_bet = 0

            if self.player.balance == 0:
                print("You're out of money!")
                print(f"Rounds played: {self.rounds_played}")
                print(f"Player wins: {self.player_wins}")
                print(f"Dealer wins: {self.dealer_wins}")
                return False

            self.play_game()

            self.rounds_played += 1

            print(f"Your balance: ${self.player.balance}")

            play_again = qst.select('Do you want to play again?',
                choices = ['Yes', 'No']).ask()
            
            if play_again == 'No':
                print("Thanks for playing! Goodbye!")
                self.display_stats()
                return False
            else:
                print("Let's play again!")
                continue

    def display_stats(self):
        print(f"Rounds played: {self.rounds_played}")
        print(f"Player wins: {self.player_wins}")
        print(f"Dealer wins: {self.dealer_wins}")
        print(f"Player funds: {self.player.balance}")
            
name = input("Welcome, please enter your name: ")
player = Player(name)
player.balance = int(input(f"Hello {player.name}! How much money do you want to start with? $"))
dealer = Dealer()

game = Game(player, dealer)
game.game_loop()