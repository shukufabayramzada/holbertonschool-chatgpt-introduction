def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.
    
    Returns:
        bool: True if there is a winner, otherwise False.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Check if the board is full (no empty spaces left).
    
    Returns:
        bool: True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Play a game of tic-tac-toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                if row in [0, 1, 2]:
                    break
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get valid column input
        while True:
            try:
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if col in [0, 1, 2]:
                    break
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Place the move if the spot is available
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()
