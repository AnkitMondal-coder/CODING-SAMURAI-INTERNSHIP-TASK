import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Tic-Tac-Toe AI (You are 'X', AI is 'O')")
    print_board(board)
    
    while True:
        # Player move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter row and column as two numbers between 0 and 2.")
        
        print_board(board)
        if check_winner(board) == "X":
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        
        # AI move
        print("AI is making a move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)
        
        if check_winner(board) == "O":
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
