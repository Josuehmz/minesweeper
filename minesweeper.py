import random

def create_board(rows, cols, bombs):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    bombs_planted = 0
    while bombs_planted < bombs:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != -1:
            board[row][col] = -1
            bombs_planted += 1
    return board

def print_board(board):
    print("   ", end="")
    for i in range(len(board[0])):
        print(f"{i:2d}", end="")
    print()
    print("  ──" + "──" * len(board[0]))
    for i in range(len(board)):
        print(f"{i:2d}|", end="")
        for j in range(len(board[0])):
            if board[i][j] == -2:
                print(" F", end="")
            elif board[i][j] >= 0:
                print(f" {board[i][j]}", end="")
            else:
                print(" X", end="")
        print()

def count_adjacent_bombs(board, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == -1:
                count += 1
    return count

def reveal_cells(board, row, col):
    if board[row][col] == -1:
        return False
    elif board[row][col] > 0:
        return True
    else:
        board[row][col] = count_adjacent_bombs(board, row, col)
        if board[row][col] == 0:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 0:
                        reveal_cells(board, i, j)
        return True

def play_game(rows, cols, bombs):
    board = create_board(rows, cols, bombs)
    game_over = False
    while not game_over:
        print_board(board)
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))
        action = input("Enter action (r for reveal, f for flag): ")
        if action == "r":
            game_over = not reveal_cells(board, row, col)
        elif action == "f":
            if board[row][col] == -2:
                board[row][col] = 0
            elif board[row][col] == 0:
                board[row][col] = -2
            else:
                print("Invalid action!")
        else:
            print("Invalid action!")
    print_board(board)
    print("Game over!")

if __name__ == "__main__":
    print("Welcome to Minesweeper!")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    bombs = int(input("Enter number of bombs: "))
    play_game(rows, cols, bombs)