import math

def display_board(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(grid, mark):
    for row in grid:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(grid[row][col] == mark for row in range(3)):
            return True
    if all(grid[i][i] == mark for i in range(3)) or all(grid[i][2 - i] == mark for i in range(3)):
        return True
    return False

def board_filled(grid):
    return all(cell != " " for row in grid for cell in row)

def minimax_algo(grid, depth, maximizing):
    if check_winner(grid, 'X'):
        return -10 + depth
    if check_winner(grid, 'O'):
        return 10 - depth
    if board_filled(grid):
        return 0
    
    if maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if grid[i][j] == " ":
                    grid[i][j] = 'O'
                    score = minimax_algo(grid, depth + 1, False)
                    grid[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if grid[i][j] == " ":
                    grid[i][j] = 'X'
                    score = minimax_algo(grid, depth + 1, True)
                    grid[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(grid):
    optimal_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = 'O'
                move_score = minimax_algo(grid, 0, False)
                grid[i][j] = " "
                if move_score > optimal_score:
                    optimal_score = move_score
                    best_move = (i, j)
    return best_move

def start_game():
    grid = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        display_board(grid)
        row, col = map(int, input("Enter your move (row and column): ").split())
        if grid[row][col] == " ":
            grid[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        
        if check_winner(grid, 'X'):
            display_board(grid)
            print("Congratulations! You win!")
            break
        if board_filled(grid):
            display_board(grid)
            print("It's a draw!")
            break
        
        ai_row, ai_col = find_best_move(grid)
        grid[ai_row][ai_col] = 'O'
        
        if check_winner(grid, 'O'):
            display_board(grid)
            print("AI wins! Better luck next time.")
            break
        if board_filled(grid):
            display_board(grid)
            print("It's a draw!")
            break

start_game()
