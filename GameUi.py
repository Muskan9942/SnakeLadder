import tkinter as tk
import random

# Define the board size
BOARD_SIZE = 30

# Snakes and Ladders positions
snakes = {14: 7, 24: 4}
ladders = {3: 22, 8: 26}

# Player positions
player_positions = [0, 0]
current_player = 0

def roll_dice():
    global current_player
    roll = random.randint(1, 6)
    result_label.config(text=f"Player {current_player + 1} rolled a {roll}")
    move_player(current_player, roll)
    update_board()
    check_winner()
    current_player = 1 - current_player  # Switch turn

def move_player(player, roll):
    new_position = player_positions[player] + roll
    if new_position > BOARD_SIZE:
        return
    if new_position in snakes:
        new_position = snakes[new_position]
    elif new_position in ladders:
        new_position = ladders[new_position]
    player_positions[player] = new_position

def update_board():
    for i in range(BOARD_SIZE + 1):
        if i in player_positions:
            index = player_positions.index(i) + 1
            board_labels[i].config(text=f"P{index}", bg="lightblue")
        else:
            board_labels[i].config(text=str(i), bg="white")

def check_winner():
    for i, pos in enumerate(player_positions):
        if pos == BOARD_SIZE:
            result_label.config(text=f"Player {i + 1} wins!")
            roll_button.config(state=tk.DISABLED)
            return

# Create GUI window
root = tk.Tk()
root.title("Snake and Ladder Game")

# Create board UI
grid_frame = tk.Frame(root)
grid_frame.pack()

board_labels = {}
for i in range(BOARD_SIZE, 0, -1):
    label = tk.Label(grid_frame, text=str(i), width=5, height=2, relief="solid")
    label.grid(row=(BOARD_SIZE - i) // 10, column=(i - 1) % 10)
    board_labels[i] = label

# Dice roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Result display
result_label = tk.Label(root, text="Roll to start the game!", font=("Arial", 12))
result_label.pack()

root.mainloop()