'''
Here I'll try to do a Tic-Tac-Toe Game using dictionaries
Assigning 1 value to each cell of the 3x3 grid

'''
import os

#"drawing" the board using a dictionary
UglyBoard = {
    'top-L':' ', 'top-M':' ', 'top-R':' ',
    'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
    'bot-L':' ', 'bot-M':' ', 'bot-R':' '
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])
    
turn = 'X'

for i in range (9):
    printBoard(UglyBoard)
    print('Turn for ' + turn + '. Insert your move: ')
    move = input()
    UglyBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    os.system('clear')
    
printBoard(UglyBoard)

