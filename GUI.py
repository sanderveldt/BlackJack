import customtkinter as ctk
import Blackjack_gui as bjg

### Set-up
window = ctk.CTk()
window.geometry("800x600")
window.title("Blackjack")
game_status = 0

### Start screen
def start_button_command():                
    name = setup_name_entry.get()
    balance = setup_balance_entry.get()

    if name == "":         ### Input validation
        setup_status_label.configure(text="Please enter a name.")
        return 
    elif not balance.isdigit() or int(balance) <= 0:
        setup_status_label.configure(text="Invalid starting balance.")
        return 
    
    player = bjg.Player(name)
    player.balance = int(balance)
    dealer = bjg.Dealer()
    game = bjg.Game(player, dealer)
    setup_frame.destroy()
    bet_screen(game)
    
setup_frame = ctk.CTkFrame(window)
setup_frame.place(relx=0.5, rely=0.5, anchor="center")

setup_frame_label = ctk.CTkLabel(setup_frame, text="Welcome to Blackjack!", font=ctk.CTkFont(size=20, weight="bold"))
setup_name_label = ctk.CTkLabel(setup_frame, text="Player Name:")
setup_name_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter your name")    
setup_balance_label = ctk.CTkLabel(setup_frame, text="Starting balance:")
setup_balance_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter starting balance")
setup_status_label = ctk.CTkLabel(setup_frame, text="", text_color="red")
setup_start_button = ctk.CTkButton(setup_frame, text="Start Game", command=start_button_command)

setup_frame_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

setup_name_label.grid(row=2, column=0, sticky="w", padx=(0, 10))
setup_name_entry.grid(row=2, column=1,)
setup_balance_label.grid(row=3, column=0, sticky="w", padx=(0, 10))
setup_balance_entry.grid(row=3, column=1,)
setup_status_label.grid(row=4, column=0, columnspan=2)
setup_start_button.grid(row=5, column=0, columnspan=2)

### Betting screen

def bet_screen(game):
    bet_frame = ctk.CTkFrame(window, border_width=2, border_color="black")
    bet_frame.place(relx=0.5, rely=0.5, anchor="center")

    bet_frame_balance = ctk.CTkLabel(bet_frame, text=f"Current Balance: ${game.player.balance}", font=ctk.CTkFont(size=16, weight="bold"))
    bet_frame_balance.grid(row=0, column=0, columnspan=3, pady=(20, 20))

    bet_frame_bet = ctk.CTkLabel(bet_frame, text="Place your bet:")
    bet_frame_bet.grid(row=1, column=0, columnspan=3)

    options = game.lay_bet()

    if options == "DEAD":
        bet_frame_bet.configure(text="You are out of money!\n Game over!")
    else:
        def make_bet(a):
            game.place_bet(a)
            bet_frame.destroy()
            game_screen(game)

        for button, amount in enumerate(options):
            bet_button = ctk.CTkButton(
                bet_frame, 
                text=f"${amount}", 
                command=lambda a=amount: make_bet(a),
                border_width=2,
                border_color="black",
                )
            bet_button.grid(row=2 + button // 3, column=button % 3)

### Game screen

def game_screen(game):

    def update_displays(game_status):
        player_hand.configure(text="  |  ".join(game.player.hand.hand))
        dealer_hand.configure(text="  |  ".join(game.dealer.hand.hand))
        info_current_bet.configure(text=f"Current Bet: ${game.current_bet}")
        info_game_status.configure(text=game_status)
        
        if game_status in (
            "BLACKJACK! You win!", 
            "Dealer has Blackjack! You lose."
            "BUST! You lose."):
            hit_button.grid_remove()
            stand_button.grid_remove()
        else:
            hit_button.grid(row=1, column=0, sticky="e")
            stand_button.grid(row=1, column=1, sticky="w")
        
        
    def start_round():
        info_game_status.configure(text="The first cards are dealt...")
        result = game.first_deal()
        if result == "PLAYER_BLACKJACK":
            update_displays("BLACKJACK! You win!")
            end_round("PLAYER_BLACKJACK")
        elif result == "DEALER_BLACKJACK":
            update_displays("Dealer has Blackjack! You lose.")
            end_round("DEALER_BLACKJACK")
        else:
            update_displays("Your move.")


    def hit():
        result = game.player_hit()
        if result == "PLAYER_BLACKJACK":
            update_displays("BLACKJACK! You win!")
        elif result == "PLAYER_BUST":
            update_displays("BUST! You lose.")
        else:
            update_displays("Your move.")
        print('You hit.')
        

    def stand():
        game.player_stand()
        update_displays("You stand. Dealer's turn.")
        print("You stand.")



    window.grid_rowconfigure(0, weight=3)
    window.grid_rowconfigure(1, weight=2)
    window.grid_rowconfigure(2, weight=3)
    window.grid_columnconfigure(0, weight=1)

    dealer_frame = ctk.CTkFrame(window)
    dealer_frame.grid_columnconfigure(0, weight=1)

    dealer_title = ctk.CTkLabel(dealer_frame, text="Dealer", font=ctk.CTkFont(size=20, weight="bold"))
    dealer_hand_title = ctk.CTkLabel(dealer_frame, text="Cards:")
    dealer_hand = ctk.CTkLabel(dealer_frame, text="  |  ".join(game.dealer.hand.hand), font=ctk.CTkFont(size=18))

    info_frame = ctk.CTkFrame(window)
    info_frame.grid_columnconfigure(0, weight=1)
    info_frame.grid_columnconfigure(1, weight=1)

    info_game_status = ctk.CTkLabel(info_frame, text=f"{game_status}", font=ctk.CTkFont(size=16, weight="bold"))
    info_current_bet = ctk.CTkLabel(info_frame, text=f"Current Bet: ${game.current_bet}")

    hit_button = ctk.CTkButton(info_frame, text = "Hit", command = hit, fg_color="green")
    stand_button = ctk.CTkButton(info_frame, text = "Stand", command = stand, fg_color="red")

    player_frame = ctk.CTkFrame(window)
    player_frame.grid_columnconfigure(0, weight=1)
    player_title = ctk.CTkLabel(player_frame, text=f"{game.player.name}", font=ctk.CTkFont(size=20, weight="bold"))
    player_hand_title = ctk.CTkLabel(player_frame, text="Cards:")
    player_hand = ctk.CTkLabel(player_frame, text="  |  ".join(game.player.hand.hand), font=ctk.CTkFont(size=18))

    
    dealer_frame.grid(row=0, column=0, sticky="nsew")
    dealer_title.grid(row=0, column=0, stick="n", pady=(10, 10))
    dealer_hand_title.grid(row=1, column=0, sticky="n")
    dealer_hand.grid(row=2, column=0, sticky="n")

    info_frame.grid(row=1, column=0, sticky="nsew")
    info_game_status.grid(row=0, column=0, columnspan=2)
    hit_button.grid(row=1, column=0, sticky="e")
    stand_button.grid(row=1, column=1, sticky="w")
    info_current_bet.grid(row=2, column=0, columnspan=2, sticky="s")

    player_frame.grid(row=2, column=0, sticky="nsew")
    player_title.grid(row=0, column=0, sticky="n", pady=(10, 10))
    player_hand_title.grid(row=1, column=0, sticky="n")
    player_hand.grid(row=2, column=0, sticky="n", pady=(20, 10))

    start_round()
 



window.mainloop()

