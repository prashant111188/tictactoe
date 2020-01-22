"""
This is a driver program for TicTacToe. It takes user inputs and drives the game
depending on the user inputs.
"""

from tictactoe.TicTacToe import BasicTicTacToe, GetTictactoeFactory, Player
from tictactoe import settings
from view import getPlayerInfoView, takePlayerInput, inputGameMode, displayGameState

if(__name__ == "__main__"):
    #Taking Plyaer details, assigning them to appropriate objects
    print(settings.HELP_STRING)
    playerA = Player("Player 1")
    playerB = Player("Player 2")
    getPlayerInfoView(playerA)
    getPlayerInfoView(playerB)
    playerTuple = (playerA, playerB)
    playerTurn = 0
    gameMode = inputGameMode()
    #Getting the correct TicTacToe game depending on the mode
    try:
        tictactoe = GetTictactoeFactory().getTictactoeFactory(gameMode)
    except KeyboardInterrupt:
        print("There is no such mode as + " + str(gameMode))
        exit()
    while(True):
        try:
            takePlayerInput(playerTuple[playerTurn])
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
            print(playerTuple[playerTurn].getPlayerWinMessage())
            displayGameState(tictactoe)
            break
        playerTurn ^= 1
        displayGameState(tictactoe)
        if(len(tictactoe.getMoves()) == 9):
            print("The game has ended in a draw.")
            break
