import customtkinter as ctk

window = ctk.CTk()

window.geometry("800x600")
window.title("Blackjack")

window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=2)
window.grid_rowconfigure(3, weight=1)

window.grid_columnconfigure(0, weight=1)

dealer_frame = ctk.CTkFrame(window)


info_frame = ctk.CTkFrame(window)


player_frame = ctk.CTkFrame(window)


button_frame = ctk.CTkFrame(window)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)


def hit():
    print('You hit.')

hit_button = ctk.CTkButton(
    button_frame,
    text = "Hit",
    command = hit
)

def stand():
    print("You stand.")

stand_button = ctk.CTkButton(
    button_frame,
    text = "Stand",
    command = stand   
)



dealer_frame.grid(row=0, column=0, sticky="nsew")
info_frame.grid(row=1, column=0, sticky="nsew")
player_frame.grid(row=2, column=0, sticky="nsew")
button_frame.grid(row=3, column=0, sticky="nsew")
hit_button.grid(row=3, column=0, sticky="e")
stand_button.grid(row=3, column=1, sticky="w")



window.mainloop()

