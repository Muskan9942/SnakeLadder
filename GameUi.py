import tkinter as tk
import random

def roll_dice():
    roll = random.randint(1, 6)
    result_label.config(text=f"You rolled a {roll}")

def create_ui():
    global result_label
    
    root = tk.Tk()
    root.title("Snake and Ladder Game")
    
    roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 14))
    roll_button.pack(pady=20)
    
    result_label = tk.Label(root, text="Click 'Roll Dice' to play", font=("Arial", 12))
    result_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_ui()
