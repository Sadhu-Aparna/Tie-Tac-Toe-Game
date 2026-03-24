import random 
board = ['-'] * 9
gameRunning = True

# Print board
def printBoard():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

# Check winner
def checkWin(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False   

# Check tie
def checkTie():
    return "-" not in board

# Player move
def playerMove():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if 0 <= pos <= 8 and board[pos] == "-":
                board[pos] = 'X'
                break
            else:
                print("Invalid move, try again.")
        except:
            print("Enter a valid number!")

# Computer move
def computerMove():
    
    # Try to win
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"   
            if checkWin("O"):
                return
            board[i] = "-"

    # Block player
    for i in range(9):
        if board[i] == "-":
            board[i] = "X"
            if checkWin("X"):
                board[i] = "O"
                return
            board[i] = "-"

    # Random move
    available = [i for i in range(9) if board[i] == "-"]
    move = random.choice(available)
    board[move] = "O"

# Game loop
while gameRunning:
    printBoard()
    playerMove()

    if checkWin("X"):
        printBoard()
        print("You Win!")
        break

    if checkTie():
        printBoard()
        print("It's a tie!")
        break

    computerMove()

    if checkWin("O"):
        printBoard()
        print("Computer Wins!")
        break

    if checkTie():
        printBoard()
        print("It's a tie!")
        break
    