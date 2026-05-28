import customtkinter as ctk

window = ctk.CTk()

window.geometry("800x800")
window.title("Blackjack")

def hit():
    print('You hit.')

hit_button = ctk.CTkButton(
    window,
    text = "Hit",
    command = hit
)

def stand():
    print("You stand.")

stand_button = ctk.CTkButton(
    window,
    text = "Stand",
    command = stand
    
)

hit_button.pack(padx=10,pady=10)
stand_button.pack(padx=100,pady=10)

title = ctk.CTkLabel(window, text = "Blackjack")
title.pack(pady=100)

window.mainloop()

