import random
import os
import pickle

# Constants
GRID_SIZE_MIN = 3
GRID_SIZE_MAX = 6

# Initialize high scores and leaderboard
high_scores = {}
leaderboard = {}

# Load existing high scores and leaderboard from a file if available
if os.path.exists("high_scores.dat"):
    with open("high_scores.dat", "rb") as file:
        high_scores = pickle.load(file)

if os.path.exists("leaderboard.dat"):
    with open("leaderboard.dat", "rb") as file:
        leaderboard = pickle.load(file)


# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" | ".join(map(str, row)))
        print("-" * (GRID_SIZE * 6 - 1))


# Function to add a new tile (2 or 4) to the grid
def add_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])


# Function to check if the game is over
def is_game_over(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return False
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return False
    return True


# Function to update the high scores and leaderboard
def update_scores(score, player_name):
    high_scores[player_name] = score
    leaderboard[player_name] = score
    sorted_leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)}

    # Save high scores and leaderboard to files
    with open("high_scores.dat", "wb") as file:
        pickle.dump(high_scores, file)

    with open("leaderboard.dat", "wb") as file:
        pickle.dump(sorted_leaderboard, file)


# Main game loop
while True:
    try:
        GRID_SIZE = int(input(f"Enter grid size ({GRID_SIZE_MIN}-{GRID_SIZE_MAX}): "))
        if GRID_SIZE < GRID_SIZE_MIN or GRID_SIZE > GRID_SIZE_MAX:
            print(f"Grid size must be between {GRID_SIZE_MIN} and {GRID_SIZE_MAX}.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
score = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Current Score: {score}")
    print_grid(grid)

    if is_game_over(grid):
        player_name = input("Game Over! Enter your name: ")
        update_scores(score, player_name)
        print("High Scores:")
        for name, high_score in high_scores.items():
            print(f"{name}: {high_score}")
        print("Leaderboard:")
        for name, leaderboard_score in leaderboard.items():
            print(f"{name}: {leaderboard_score}")
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    direction = input("Enter direction (w/a/s/d): ").lower()

    if direction not in ['w', 'a', 's', 'd']:
        continue

    # Perform tile movements here based on the direction input
    # Update the grid and score accordingly
    # You need to implement this part of the code

    # Add a new tile after each move
    add_tile(grid)
