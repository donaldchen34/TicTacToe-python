#Donald Chen
#TicTacToe
#Was written for the purpose of learning python syntax

import copy
import random
import sys



#************
#BOARD CONFIG
#************
theBoard  = {
             'TOP-L' : ' ', 'TOP-M' : ' ','TOP-R' : ' ',
             'MID-L' : ' ', 'MID-M' : ' ','MID-R' : ' ',
             'BOT-L' : ' ', 'BOT-M' : ' ','BOT-R' : ' '      
             }

#Prints tictactoe Board
def printBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'] + '\n' +
          "-----" + '\n' +
          board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'] + '\n' +
          "-----" + '\n' +
          board['BOT-L'] + '|' + board['BOT-M'] + '|' + board['BOT-R'] 
          )
    
#Checks for three in a row
def isWinner(board, piece):
    threeInARow = False
      
    if (#Three in a Row
        #Horizontal
        board['TOP-L'] == piece and board['TOP-M'] == piece and board['TOP-R'] == piece or
        board['MID-L'] == piece and board['MID-M'] == piece and board['MID-R'] == piece or
        board['BOT-L'] == piece and board['BOT-M'] == piece and board['BOT-R'] == piece or 
        #Vertical
        board['TOP-L'] == piece and board['MID-L'] == piece and board['BOT-L'] == piece or
        board['TOP-M'] == piece and board['MID-M'] == piece and board['BOT-M'] == piece or
        board['TOP-R'] == piece and board['MID-R'] == piece and board['BOT-R'] == piece or
        #Diagnol
        board['TOP-L'] == piece and board['MID-M'] == piece and board['BOT-R'] == piece or
        board['TOP-R'] == piece and board['MID-M'] == piece and board['BOT-L'] == piece 
        ):
        threeInARow = True

    return threeInARow
 
#Returns if board is full
def boardIsFull(board):
    for position in board:
        if board[position] == ' ':
            return False
       
    return True

#Clears board for another round
def clearBoard(board):
    for position in board:
        board[position] = ' '

#*************
#PLAYER OPTIONS
#*************

#Asks player for choice (X or O)
def pickPiece():
    print('Do you want to be X or O.')
    choice = input().upper()

    validChoice = False 
    if choice == 'O' or choice == 'X':
        validChoice = True

    while not validChoice:   
        print('Invalid Choice, Please Choose X or O.')
        choice = input().upper()
        if choice == 'X' or choice == 'O':
            validChoice = True

    return choice

#Takes input from player as move
def playerMove(board, playerPiece):
    printBoard(board)
    print('Choose a square to place your piece. (top,mid,bot, - L,M,R ie top-L )')
    square = input().upper()

    validLocation  = False

    while not validLocation:
        if square not in board:
            print('Invalid square, Choose a correct spot')
            square = input().upper()
        elif board[square] != ' ':
            print ('Square Taken, Choose another spot')
            square = input().upper()
        else:
            validLocation = True

    if validLocation:
        board[square] = playerPiece



#*************
#COMPUTER OPTIONS
#*************
def computerMove(board, computerPiece, playerPiece):
    

    #Check if computer can win
    #Creates copy of board and checks if all positions to see
    #if computer wins. If true places the piece in the real board
    for position in board:
        if board[position] == ' ':
            boardCopy = copy.deepcopy(board)
            boardCopy[position] = computerPiece
            if isWinner(boardCopy, computerPiece) == True:
                board[position] = computerPiece
                return None

    #Check if human can win
    #Creates copy of board and checks if all positions to see
    #if player wins. If true places the piece in the real board
    for position in board:
        if board[position] == ' ':
            boardCopy = copy.deepcopy(board)
            boardCopy[position] = playerPiece
            if isWinner(boardCopy, playerPiece) == True:
                board[position] = computerPiece
                return None

    #Take Middle 
    if board['MID-M'] == ' ':
        board['MID-M'] = computerPiece
        return None

    #Take Corner
    #Randomly chooses a corner that is open

    corners = ['TOP-L', 'TOP-R', 'BOT-L', 'BOT-R']
    #Checks which corner are open
    for position in corners:
        if board[position] != ' ':
            corners.remove(position)
    #Randomly chooses a corner
    if len(corners) > 0:
        move = random.randint(0, len(corners) - 1)
        board[corners[move]] = computerPiece
        return None


    #Take Sides
    #Randomly chooses a side that is open

    sides = ['TOP-M', 'MID-L','MID-R', 'BOT-M']
    #Checks which sides are open
    for position in sides:
        if board[position] != ' ':
            sides.remove(position)
    #Randomly chooses a side
    if len(sides) > 0:
        move = random.randint(0, len(corners) - 1)
        board[sides[move]] = computerPiece
        return None


#**************
#GAME SETTINGS
#**************

#Return number 1 or 2
def whoGoesFirst():
    return random.randint(1,2)


#Play Game
#Asks player who is first
#Game is played until winner is found or board is full
#Prints output of game and asks for another game
def playTicTacToe():
    playerPiece = pickPiece() # If player wants X or O
    computerPiece = ''

    #Determines ComputerPiece
    if playerPiece == 'X':
        computerPiece = 'O'
    else:
        computerPiece = 'X'

    #Determines who goes first:
    #1 is Player
    #2 is Computer
    turn = whoGoesFirst()

    #Output who goes first
    if turn == 1:
        print('You get first move')
    else:
        print('Computer has the first move')

    #Play Game
    #Ends if board is full or someone wins
    #Determines whose turn with the turn counter (1 = Player, 2 = Computer)
    while(boardIsFull(theBoard) or isWinner(theBoard,computerPiece) or isWinner(theBoard,playerPiece)) is False:
        if turn % 2 == 1:
            playerMove(theBoard,playerPiece)
            turn += 1
        else:
            computerMove(theBoard,computerPiece,playerPiece)
            turn += 1 

    #Print End of Game
    printBoard(theBoard)
    if boardIsFull(theBoard):
        print('Game is a draw. The board is full')
    elif(isWinner(theBoard,playerPiece)):
        print('Congratutaions, You won!')
    elif(isWinner(theBoard,computerPiece)):
        print('The Computer won')


    #Play Again?
    print('Do you want to play again? (Yes or No)')
    playAgain = input().lower()

    if playAgain == 'yes':
        clearBoard(theBoard)
        playTicTacToe()
        
    if playAgain == 'no':
        sys.exit('Thank you for playing')


#******
#MAIN
#******

def main():
    
    playTicTacToe()



if __name__ == '__main__':
    main()