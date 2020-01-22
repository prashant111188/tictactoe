"""
This file handles the input output for the tictactoe game
"""

from tictactoe.TicTacToe import BasicTicTacToe, GetTictactoeFactory, Player
from tictactoe import settings

def takePlayerInput(player):
    """
    This function takes player inputs and assigns to the player object
    """
    print(player.getPlayerName() + " enters the game cell X where you want to make the move:")
    moveX = int(input())
    print(player.getPlayerName() + " enters the game cell Y where you want to make the move:")
    moveY = int(input())
    currentMove = (moveX, moveY)
    print("Please enter the move value:")
    currentMoveVal = input()
    player.setCurrentMove(currentMove)
    player.setCurrentMoveVal(currentMoveVal)

def getPlayerInfoView(player):
    """
    This function takes generic player information and sets to the Player object
    """
    print("Please enter your name " + player.getPlayerDesignation() + ":")
    name = input()
    player.setInfo(name)

def inputGameMode():
    """
    This function takes the game mode and returns it to the game driver
    """
    try:
        gameMode = int(input("Please select the game mode: Either '1' for pattern based mode or '2' for number based mode:"))
    except:
        print("You seem to have entered a non-integer mode. Please enter either 1 or 2")
        exit()
    return gameMode

def displayGameState(gameBoard):
    """
    This function diaplays the current game state
    """
    print("\n\nThe Game state after last move:")
    gameBoard.displayGameBoard()
