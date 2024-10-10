board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Function to print the board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

# Check if a position is free
def spaceFree(pos):
    return board[pos] == ' '

# Check if there is a win
def checkWin():
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

# Check if it's a draw
def checkDraw():
    return all(space != ' ' for space in board.values())

# Insert the letter into the board
def insertLetter(letter, position):
    if spaceFree(position):
        board[position] = letter
        printBoard(board)
        if checkWin():
            if letter == 'X':
                print('Bot wins!')
            else:
                print('You win!')
            return True  # Return True if someone won
        if checkDraw():
            print('Draw!')
            return True  # Return True if it's a draw
        return False
    else:
        print('Position taken, please pick a different position.')
        return False

# Player's move
def playerMove():
    position = int(input('Enter position for O (1-9): '))
    while not spaceFree(position):
        position = int(input('Enter valid position for O (1-9): '))
    insertLetter('O', position)

# Computer's move using minimax algorithm
def compMove():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter('X', bestMove)

# Minimax algorithm to decide the computer's move
def minimax(board, isMaximizing):
    if checkWin():
        if isMaximizing:
            return -1
        else:
            return 1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# Main game loop
while True:
    if not checkWin() and not checkDraw():
        compMove()
    if not checkWin() and not checkDraw():
        playerMove()
    if checkWin() or checkDraw():
        break
