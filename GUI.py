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
    
    player = bjg.Player(name)          ### Game initialization
    player.balance = int(balance)
    dealer = bjg.Dealer()
    game = bjg.Game(player, dealer)
    setup_frame.destroy()
    game_screen(game)
    game_status += 1
    
setup_frame = ctk.CTkFrame(window)
setup_frame.place(relx=0.5, rely=0.5, anchor="center")

setup_frame_label = ctk.CTkLabel(setup_frame, text="Welcome to Blackjack!")
setup_name_label = ctk.CTkLabel(setup_frame, text="Player Name:")
setup_name_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter your name")    
setup_balance_label = ctk.CTkLabel(setup_frame, text="Starting balance:")
setup_balance_entry = ctk.CTkEntry(setup_frame, placeholder_text="Enter starting balance")
setup_status_label = ctk.CTkLabel(setup_frame, text="", text_color="red")
setup_start_button = ctk.CTkButton(setup_frame, text="Start Game", command=start_button_command)

setup_frame_label.grid(row=0, column=0, columnspan=2)
setup_name_label.grid(row=1, column=0)
setup_name_entry.grid(row=1, column=1)
setup_balance_label.grid(row=2, column=0)
setup_balance_entry.grid(row=2, column=1)
setup_status_label.grid(row=3, column=0, columnspan=2)
setup_start_button.grid(row=4, column=0, columnspan=2)

### Betting screen

def bet_screen(game):
    bet_frame = ctk.CTkFrame(window)
    bet_frame.place(relx=0.5, rely=0.5, anchor="center")
    bet_frame_balance = ctk.CTkLabel(bet_frame, text=f"Current Balance: ${game.player.balance}")
    bet_frame_bet = ctk.CTkLabel(bet_frame, text="Place your bet:")


### Game screen


def game_screen(game):

    window.grid_rowconfigure(0, weight=2)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=2)
    window.grid_rowconfigure(3, weight=1)
    window.grid_columnconfigure(0, weight=1)

    dealer_frame = ctk.CTkFrame(window)
    dealer_frame.grid_columnconfigure(0, weight=1)

    dealer_title = ctk.CTkLabel(dealer_frame, text="Dealer")
    dealer_hand = ctk.CTkTextbox(dealer_frame)

    info_frame = ctk.CTkFrame(window)


    player_frame = ctk.CTkFrame(window)

    player_textbox = ctk.CTkTextbox(player_frame)

    button_frame = ctk.CTkFrame(window)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

    def hit():
        bjg.game.player_hit()
        print('You hit.')

    def stand():
        bjg.game.player_stand()
        print("You stand.")


    hit_button = ctk.CTkButton(button_frame, text = "Hit", command = hit)
    stand_button = ctk.CTkButton(button_frame, text = "Stand", command = stand)

    dealer_frame.grid(row=0, column=0, sticky="nsew")
    dealer_title.grid(row=0, column=0, stick="n")

    info_frame.grid(row=1, column=0, sticky="nsew")

    player_frame.grid(row=2, column=0, sticky="nsew")

    button_frame.grid(row=3, column=0, sticky="nsew")
    hit_button.grid(row=3, column=0, sticky="e")
    stand_button.grid(row=3, column=1, sticky="w")



window.mainloop()

