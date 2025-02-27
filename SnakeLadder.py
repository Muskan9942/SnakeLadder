import random

# Define the board size
BOARD_SIZE = 30

# Snakes and Ladders positions (start -> end)
snakes = {14: 7, 24: 4}
ladders = {3: 22, 8: 26}

# Initialize player positions
player_positions = [0, 0]

def roll_dice():
    return random.randint(1, 6)

def move_player(player, roll):
    new_position = player_positions[player] + roll
    if new_position > BOARD_SIZE:
        new_position = BOARD_SIZE
    if new_position in snakes:
        new_position = snakes[new_position]
        print(f"Player {player + 1} got bitten by a snake! Moved to {new_position}")
    elif new_position in ladders:
        new_position = ladders[new_position]
        print(f"Player {player + 1} climbed a ladder! Moved to {new_position}")
    player_positions[player] = new_position

def print_board():
    for i in range(1, BOARD_SIZE + 1):
        if i in player_positions:
            player = player_positions.index(i) + 1
            print(f"P{player}", end="\t")
        else:
            print(i, end="\t")
        if i % 10 == 0:
            print()

def main():
    current_player = 0
    while True:
        print(f"\nPlayer {current_player + 1}'s turn")
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"Player {current_player + 1} rolled a {roll}")
        move_player(current_player, roll)
        print_board()
        if player_positions[current_player] == BOARD_SIZE:
            print(f"Player {current_player + 1} wins!")
            break
        current_player = 1 - current_player

if __name__ == "__main__":
    main()