"""
This module contains the class definitions for
Abstract tictactoe, Basic tictactoe, Sum tictactoe
"""
from tictactoe import settings

class AbstractTicTacToe:
    def __init__(self):
        """
        Initialize for AbstractTicTacToe
        PARAMS:
        self: object
        RETURNS:
        Initialized object
        """
        self.gameWinnerBoard = {"row":    {
                                    0:{"inputCount":0, "finishedGame":0},
                                    1:{"inputCount":0, "finishedGame":0},
                                    2:{"inputCount":0, "finishedGame":0}
                                    },
                          "column": {
                                    0:{"inputCount":0, "finishedGame":0},
                                    1:{"inputCount":0, "finishedGame":0},
                                    2:{"inputCount":0, "finishedGame":0}
                                    },
                          "diag":   {
                                    0:{"inputCount":0, "finishedGame":0},
                                    2:{"inputCount":0, "finishedGame":0}
                                    }
                        }
        self.moves = []
        self.displayBoard = [[0,0,0],[0,0,0],[0,0,0]]

    def getValidMoveMessage(self):
        """
        This method returns the validation faliure message
        PARAMS:
        self:current object
        """
        return "Invalid Move"

    def setMoves(self, move):
        """
        This method adds the current move to the total moves
        for the board
        PARAMS:
        self:current object
        move:current move
        RETURNS:
        Nothing
        """
        self.moves.append(move)

    def getMoves(self):
        """
        This method is a getter method for total moves
        PARAMS:
        self:current object
        RETURNS:
        self.moves : List
        """
        return self.moves

    def validateMove(self, playerTurn, move, moveVal):
        """
        This method validates the move
        PARAMS:
        self:current object
        playerTurn:Player Turn
        move:current move
        moveVal: value of the move
        RETURNS:
        Boolean whether move is a valid one for the board
        """
        if(move in self.moves):
            return False

    def displayGameBoard(self):
        """
        Method to display the Game Board
        PARAMS:
        self:current object
        RETURNS:
        Nothing
        """
        for row in range(len(self.displayBoard)):
            print(self.displayBoard[row])

    def updateBoard(self, playerTurn, move, playerInput):
        """
        The method updates the game board with validated validated
        user input.
        PARAMS:
        self:current object
        move:player move tuple
        playerInput:player input value
        RETURNS:
        Returns nothing. Updates the object's game board
        """
        self.gameWinnerBoard["row"][move[0]]["inputCount"] += 1
        self.gameWinnerBoard["row"][move[0]]["finishedGame"] += playerInput
        self.gameWinnerBoard["column"][move[1]]["inputCount"] += 1
        self.gameWinnerBoard["column"][move[1]]["finishedGame"] += playerInput
        if((move[0] - move[1]) == 0):
            self.gameWinnerBoard["diag"][0]["inputCount"] += 1
            self.gameWinnerBoard["diag"][0]["finishedGame"] += playerInput
        if((move[0] + move[1] == 2)):
            self.gameWinnerBoard["diag"][2]["inputCount"] += 1
            self.gameWinnerBoard["diag"][2]["finishedGame"] += playerInput
        self.setMoves(move)

    def validateBoard(self, move, player):
        """
        This method is Basic tictactoe validateBoard
        implementation.
        It checks the updated gameWinnerBoard and if input count for a
        row, column or diagnoal is 3, checks if the sum of the inputs is 3 or 6
        PARAMS:
        self:current object
        move:player move tuple
        player:Player object currently operating the game board
        RETURNS:
        Boolean if current input has won the game
        """
        if(self.gameWinnerBoard["row"][move[0]]["inputCount"] == 3 and (self.gameWinnerBoard["row"][move[0]]["finishedGame"] in self.gameValidationSum)):
            #print("row")
            player.setWinner(True)
        if(self.gameWinnerBoard["column"][move[1]]["inputCount"] == 3 and (self.gameWinnerBoard["column"][move[1]]["finishedGame"] in self.gameValidationSum)):
            #print("column" + str(move[1]))
            player.setWinner(True)
        if(self.gameWinnerBoard["diag"][0]["inputCount"] == 3 and (self.gameWinnerBoard["diag"][0]["finishedGame"] in self.gameValidationSum)):
            #print("diag1")
            player.setWinner(True)
        if(self.gameWinnerBoard["diag"][2]["inputCount"] == 3 and (self.gameWinnerBoard["diag"][2]["finishedGame"] in self.gameValidationSum)):
            #print("diag2")
            player.setWinner(True)

class BasicTicTacToe(AbstractTicTacToe):
    def __init__(self):
        """
        Initialize for BasicTicTacToe
        PARAMS:
        self:current object
        RETURNS:
        Initialized object
        """
        AbstractTicTacToe.__init__(self)
        self.moveArray = {0:1, 1:2}
        self.validMoveActual = {0:'x', 1:'o'}
        self.gameValidationSum = settings.SUM_TICTACTOE_BASIC

    def updateBoard(self, playerTurn, move, playerInput):
        """
        The method updates the game board with validated validated
        user input.
        PARAMS:
        self:current object
        move:player move tuple
        playerInput:player input value
        RETURNS:
        Returns nothing. Updates the object's game board
        """
        super().updateBoard(playerTurn, move, self.moveArray[playerTurn])
        self.displayBoard[move[0]][move[1]] = self.validMoveActual[playerTurn]

    def getGameValidationSum(self):
        """
        Getter method for gameValidationSum
        PARAMS:
        self:current object
        RETURNS:
        game validation sum
        """
        return self.gameValidationSum

    def validateMove(self, playerTurn, move, moveVal):
        """
        This method validates the current move made by the player
        PARAMS:
        self:current object
        playerTurn:Player Turn
        moveVal:Value of the move
        move:current move
        RETURNS:
        Boolean whether the move is the valid one for the board
        """
        if(not ((0 <= move[0] <= 2) and (0 <= move[1] <= 2))):
            return False
        if(move in self.moves):
            #print(self.moves)
            return False
        if(self.validMoveActual[playerTurn] != moveVal):
            #print(moveVal)
            return False
        return True

    def getValidMoveMessage(self):
        """
        This method returns the validation faliure message
        PARAMS:
        self:current object
        """
        return "This mode allows only 'x' and 'o' values.\nAlso, Player 1 should input 'x' and player 2 'o'"

class SumTictactoe(AbstractTicTacToe):
    def __init__(self):
        """
        Initialize for SumTictactoe
        PARAMS:
        self:current object
        RETURNS:
        Initialized object
        """
        AbstractTicTacToe.__init__(self)
        self.validMoveActual = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        self.gameValidationSum = settings.SUM_TICTACTOE_SUM

    def updateBoard(self, playerTurn, move, playerInput):
        """
        The method updates the game board with validated validated
        user input.
        PARAMS:
        self:current object
        move:player move tuple
        playerInput:player input value
        RETURNS:
        Returns nothing. Updates the object's game board
        """
        playerInput = int(playerInput)
        super().updateBoard(playerTurn, move, playerInput)
        self.displayBoard[move[0]][move[1]] = playerInput
        self.validMoveActual[playerInput] = 1

    def getGameValidationSum(self):
        """
        Getter method for gameValidationSum
        PARAMS:
        self:current object
        RETURNS:
        game validation sum
        """
        return self.gameValidationSum

    def validateMove(self, playerTurn, move, moveVal):
        """
        This method validates the current move made by the player
        PARAMS:
        self:current object
        playerTurn:Player Turn
        moveVal:Value of the move
        move:current move
        RETURNS:
        Boolean whether the move is the valid one for the board
        """
        if(not ((0 <= move[0] <= 2) and (0 <= move[1] <= 2))):
            return False
        moveVal = int(moveVal)
        if(move in self.moves):
            return False
        if((self.validMoveActual[moveVal] == 1) or not (1 <= moveVal <= 9)):
            return False
        if((playerTurn%2 == 0 and moveVal%2 == 0) or (playerTurn%2 != 0 and moveVal%2 != 0)):
            return False
        return True

    def getValidMoveMessage(self):
        """
        This method returns the validation faliure message
        PARAMS:
        self:current object
        """
        return "For this mode, player 1 should enter odd numbers between 1-9 and player 2 should enter even numbers between 2-8."

class GetTictactoeFactory():
    def __init__(self):
        """
        Initialize for SumTictactoe
        PARAMS:
        self:current object
        RETURNS:
        Initialized object
        """
        pass

    def getTictactoeFactory(self, mode):
        """
        This method returns appropriate AbstractTicTacToe
        depending on the user input
        PARAMS:
        self:current object
        mode:Game mode
        """
        if(mode == settings.BASICMODE):
            return BasicTicTacToe()
        elif(mode == settings.SUMMODE):
            return SumTictactoe()
        else:
            raise KeyboardInterrupt

class Player():
    def __init__(self, playerDesignation):
        """
        Initialize the player
        PARAMS:
        self:Current player object
        RETURNS:
        Initialized object
        """
        self.moves = []
        self.currentMove = ()
        self.currentMoveVal = None
        self.winner = False
        self.name = "__NO_NAME__"
        self.playerDesignation = playerDesignation

    def setInfo(self, *args):
        """
        This method sets the player information
        PARAMS:
        self:current object
        args:Just name as of now
        RETURNS:
        Nothing
        """
        self.name = args[0]

    def getPlayerName(self):
        """
        Getter method for player name
        PARAMS:
        self:current object
        RETURNS
        String player name
        """
        return self.name

    def getPlayerDesignation(self):
        """
        Getter method for player Designation
        PARAMS:
        self:current object
        RETURNS
        String player Designation
        """
        return self.playerDesignation

    def setCurrentMove(self, move):
        """
        This method sets the current move input by the player
        PARAMS:
        self:current object
        move:Move tuple
        RETURNS:
        Nothing
        """
        self.currentMove = move

    def setCurrentMoveVal(self, moveVal):
        """
        This method sets the current move value input by the player
        PARAMS:
        self:current object
        move:Move Value
        RETURNS:
        Nothing
        """
        self.currentMoveVal = moveVal

    def getCurrentMove(self):
        """
        This method returns the current move co-ordinates
        PARAMS:
        self:current object
        RETURNS:
        Current move co-ordinates
        """
        return self.currentMove

    def getCurrentMoveVal(self):
        """
        This method returns the current move value
        PARAMS:
        self:current object
        RETURNS:
        Current move value
        """
        return self.currentMoveVal

    def isWinner(self):
        """
        This method returns True if the Player is a winner
        PARAMS:
        self:current object
        RETURNS:
        Boolean self.winner
        """
        return self.winner

    def setWinner(self, winner=False):
        """
        This method sets the winner value after the current move
        PARAMS:
        self:Current object
        winner:Boolean value of winner
        RETURNS:
        Nothing
        """
        self.winner = winner

    def getPlayerWinMessage(self):
        """
        This method returns the player win Message
        PARAMS:
        self:current object
        RETURNS:
        The winning message
        """
        return "Player " + self.name + " has won the game"

if(__name__ == "__main__"):
    tictactoe = GetTictactoeFactory().getTictactoeFactory("Basic")
    print(tictactoe.gameWinnerBoard)
