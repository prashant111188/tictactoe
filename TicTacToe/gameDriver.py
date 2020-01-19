"""
This is a driver program for TicTacToe. It takes user inputs and drives the game
depending on the user inputs.
"""

from tictactoe.TicTacToe import BasicTicTacToe, GetTictactoeFactory, Player
from tictactoe import settings

if(__name__ == "__main__"):
    #Taking Plyaer details, assigning them to appropriate objects
    print(settings.HELP_STRING)
    playerA = Player("Player 1")
    playerB = Player("Player 2")
    playerA.getPlayerInfo()
    playerB.getPlayerInfo()
    playerTuple = (playerA, playerB)
    playerTurn = 0
    try:
        gameMode = int(input("Please select the game mode: Either '1' for pattern based mode or '2' for number based mode:"))
    except:
        print("You seem to have entered a non-integer mode. Please enter either 1 or 2")
        exit()
    #Getting the correct TicTacToe game depending on the mode
    try:
        tictactoe = GetTictactoeFactory().getTictactoeFactory(gameMode)
    except KeyboardInterrupt:
        print("There is no such mode as + " + str(gameMode))
        exit()
    while(True):
        try:
            playerTuple[playerTurn].makeMove()
        except KeyboardInterrupt:
            exit()
        except:
            print("You seem to have entered a non-integer value. Please enter again.")
            continue
        #print(playerTuple[playerTurn].getCurrentMove())
        if(not tictactoe.validateMove(playerTurn, playerTuple[playerTurn].getCurrentMove(), playerTuple[playerTurn].getCurrentMoveVal())):
            print(tictactoe.getValidMoveMessage())
            continue
        tictactoe.updateBoard(playerTurn, playerTuple[playerTurn].getCurrentMove(), playerTuple[playerTurn].getCurrentMoveVal())
        tictactoe.validateBoard(playerTuple[playerTurn].getCurrentMove(), playerTuple[playerTurn])
        if(playerTuple[playerTurn].isWinner()):
            playerTuple[playerTurn].getPlayerWinMessage()
            tictactoe.displayGameBoard()
            break
        playerTurn ^= 1
        print("\n\nThe Game state after last move:")
        tictactoe.displayGameBoard()
        if(len(tictactoe.getMoves()) == 9):
            print("The game has ended in a draw.")
            break
