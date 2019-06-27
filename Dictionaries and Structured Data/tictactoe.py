'''
Here I'll try to do a Tic-Tac-Toe Game using dictionaries
Assigning 1 value to each cell of the 3x3 grid

'''

import os, random

#"drawing" the board using a dictionary
UglyBoard = {
    7:' ', 8:' ', 9:' ',
    4:' ', 5:' ', 6:' ',
    1:' ', 2:' ', 3:' '
}

def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

#Let the player choose between X or O. The first letter in the list is the player's one
def playerLetterIn():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('X or O, choose one for you: ')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

#Choose who start firs
def startingPlayer():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

#Do you want to replay?
def replay():
    print('Wanna replay? (yes or no): ')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

#Feeding the board(bo) to this function let you if there's a winner returning TRUE
def win(bo, lett):
    return ((bo[7] == lett and bo[8] == lett and bo[9] == lett) or # 3 in the top
        (bo[4] == lett and bo[5] == lett and bo[6] == lett) or # 3 in the middle
        (bo[1] == lett and bo[2] == lett and bo[3] == lett) or # 3 in the bottom
        (bo[7] == lett and bo[4] == lett and bo[1] == lett) or # column on the left side
        (bo[8] == lett and bo[5] == lett and bo[2] == lett) or # column in the middle
        (bo[9] == lett and bo[6] == lett and bo[3] == lett) or # column on the right side
        (bo[7] == lett and bo[5] == lett and bo[3] == lett) or # first diagonal
        (bo[9] == lett and bo[5] == lett and bo[1] == lett)) # second diagonal

#cloning the board to be sure not to f'up anything
def boardClone(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

#Check if the cell is not set yet.
def isItFree(board, move):
    return board[move] == ' '

# Return True if every space on the board has been taken. Otherwise return False.
def isBoardFull(board):
    for i in range(1, 10):
        if isItFree(board, i):
            return False
    return True

#Let the player have a choice
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isItFree(board, int(move)):
        print('Pick your next move: (1-9)')
        move = input()
    return int(move)

#Returning a valid move on the board, NONE if there is none.
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isItFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Choose the "best move" out of the grid.
def getComputerMove(board, iaLetter):
    if iaLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if winning is possible in 1 move
    for i in range(1, 10):
        copy = boardClone(board)
        if isItFree(copy, i):
            makeMove(copy, iaLetter, i)
            if win(copy, iaLetter):
                return i

    # Then, check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = boardClone(board)
        if isItFree(copy, i):
            makeMove(copy, playerLetter, i)
            if win(copy, playerLetter):
                return i

    # Try taking the corners, if free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try taking the center, if free.
    if isItFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


print("Welcome to Tris! I'm italian so this is our name!")

while True:
    # Reset the board
    UglyBoard = [' '] * 10
    playerLetter, iaLetter = playerLetterIn()
    turn = startingPlayer()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            printBoard(UglyBoard)
            move = getPlayerMove(UglyBoard)
            makeMove(UglyBoard, playerLetter, move)

            if win(UglyBoard, playerLetter):
                printBoard(UglyBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(UglyBoard):
                    printBoard(UglyBoard)
                    print('The game is a tie!')
                    break
                else:
                    os.system('cls')
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(UglyBoard, iaLetter)
            makeMove(UglyBoard, iaLetter, move)

            if win(UglyBoard, iaLetter):
                printBoard(UglyBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(UglyBoard):
                    printBoard(UglyBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not replay():
        break