import random

# Initialize the game board
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    return board

# Add a new tile (2 or 4) to the board
def add_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

# Print the game board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Slide tiles in a row or column
def slide(row):
    new_row = [0] * 4
    j = 0
    for i in range(4):
        if row[i] != 0:
            new_row[j] = row[i]
            j += 1
    return new_row

# Merge tiles in a row or column
def merge(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

# Perform a move (left, right, up, or down) on the board
def move(board, direction):
    if direction == "left":
        for i in range(4):
            board[i] = slide(board[i])
            board[i] = merge(board[i])
            board[i] = slide(board[i])
    elif direction == "right":
        for i in range(4):
            board[i] = slide(board[i][::-1])[::-1]
            board[i] = merge(board[i])[::-1]
            board[i] = slide(board[i][::-1])[::-1]
    elif direction == "up":
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            column = slide(column)
            column = merge(column)
            column = slide(column)
            for i in range(4):
                board[i][j] = column[i]
    elif direction == "down":
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            column = slide(column[::-1])[::-1]
            column = merge(column[::-1])[::-1]
            column = slide(column[::-1])[::-1]
            for i in range(4):
                board[i][j] = column[i]

# Check if the game is over
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return False

    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j]:
                return False

    return True

# Main game loop
def main():
    board = initialize_board()
    add_tile(board)
    add_tile(board)
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        direction = input("Enter move (left, right, up, down): ").lower()
        if direction in ["left", "right", "up", "down"]:
            move(board, direction)
            add_tile(board)
        else:
            print("Invalid move. Please enter left, right, up, or down.")

if __name__ == "__main__":
    main()
