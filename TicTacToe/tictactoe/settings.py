"""
Settings file to keep global game settings
"""

BASICMODE = 1
SUMMODE = 2
PLAYER_COUNT = 2
BASIC_TICTACTOE_VALID_MOVES = ('x', 'o')
SUM_TICTACTOE_BASIC = [3,6]
SUM_TICTACTOE_SUM = [15]
HELP_STRING = """
Let's play Tic Tac Toe. :D :D :D

Rules:
There are two modes to this game:

1] Pattern Based
2] Number Based

1] Pattern based game is the regular tic tac toe where two users enter 'x' and 'o'
The first player to get a row, column or diagonal filled with his/ her patter wins.

2] First user places any odd number from 1-9 and second user places any even number
from 2-8.
The first player to get a sum of 15 in a row, column or diagonal wins.
The row, column, diagonal can contain numbers entered by other players as well.
Finaly, No digit can be repeated.

Let's Start
"""
