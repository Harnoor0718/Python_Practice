import tkinter as tk
import random

# Game logic function
def check_win(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif (player == 0 and computer == 1) or \
         (player == 1 and computer == 2) or \
         (player == 2 and computer == 0):
        return "You Win!"
    else:
        return "You Lose!"

# Handle user's choice
def play(choice):
    player = {"Snake": 0, "Water": 1, "Gun": 2}[choice]
    computer = random.randint(0, 2)
    choices = ["Snake", "Water", "Gun"]
    
    result = check_win(player, computer)
    
    result_label.config(
        text=f"You chose: {choices[player]}\n"
             f"Computer chose: {choices[computer]}\n"
             f"{result}"
    )

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("350x300")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="🐍 Snake Water Gun Game 🔫", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

snake_btn = tk.Button(button_frame, text="Snake", width=10, command=lambda: play("Snake"))
water_btn = tk.Button(button_frame, text="Water", width=10, command=lambda: play("Water"))
gun_btn = tk.Button(button_frame, text="Gun", width=10, command=lambda: play("Gun"))

snake_btn.grid(row=0, column=0, padx=10, pady=10)
water_btn.grid(row=0, column=1, padx=10, pady=10)
gun_btn.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()
