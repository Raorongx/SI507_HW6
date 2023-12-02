from enum import Enum

'''
This is the start of the HW.
If there is any conflict between the doc string and the HW document,
please follow the instruction in the HW document.
Good Luck and have fun !
'''

class Notation(Enum):
    """Enumeration for representing different types of notations in the game.

    Attributes:
        EMPTY (int): Represents an empty cell on the board.
        PLAYER1 (int): Represents a cell occupied by Player 1.
        PLAYER2 (int): Represents a cell occupied by Player 2.
    """

class Player:
    """Represents a player in the game.

    Attributes:
        __playerName (str): The name of the player.
        __playerNotation (Notation): The notation (symbol) used by the player on the board.
        __curScore (int): The current score of the player.

    Args:
        playerName (str): The name of the player.
        playerNotation (Notation): The notation (symbol) used by the player.
        curScore (int): The initial score of the player.
    """

    def __init__(self, playerName, playerNotation, curScore):
        pass

    def display(self) -> str:
        """Displays the player's details including name, notation, and current score."""
        pass

    def addScoreByOne(self):
        """Increments the player's score by one."""
        pass

    def getScore(self):
        """Returns the current score of the player."""
        pass

    def getName(self):
        """Returns the name of the player."""
        pass

    def getNotation(self):
        """Returns the notation used by the player."""
        pass

class Board:
    """Represents the game board.

    Attributes:
        __rowNum (int): Number of rows in the board.
        __colNum (int): Number of columns in the board.
        __grid (list): 2D list representing the game board.

    Args:
        rowNum (int): Number of rows in the board.
        colNum (int): Number of columns in the board.
    """

    def __init__(self, rowNum, colNum) -> None:
        pass

    def initGrid(self):
        """Initializes the game board with empty cells."""
        pass

    def getColNum(self):
        """Returns the number of columns in the board."""
        pass

    def placeMark(self, colNum, mark):
        """Attempts to place a mark on the board at the specified column.

        Args:
            colNum (int): The column number where the mark is to be placed.
            mark (Notation): The mark to be placed on the board.

        Returns:
            bool: True if the mark was successfully placed, False otherwise.
        """
        pass

    def checkFull(self):
        """Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        pass

    def display(self):
        """Displays the current state of the board."""
        pass

    # Private methods for internal use
    def __checkWinHorizontal(self, target):
        pass

    def __checkWinVertical(self, target):
        pass

    def __checkWinOneDiag(self, target, rowNum, colNum):
        pass

    def __checkWinAntiOneDiag(self, target, rowNum, colNum):
        pass

    def __checkWinDiagonal(self, target):
        pass

    def checkWin(self, target):
        """Checks if there is a winning condition on the board.

        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        pass

class Game:
    """Represents the game logic and flow.

    Args:
        rowNum (int): Number of rows in the game board.
        colNum (int): Number of columns in the game board.
        connectN (int): Number of consecutive marks needed for a win.
        targetScore (int): The score a player needs to reach to win the game.
        playerName1 (str): Name of the first player.
        playerName2 (str): Name of the second player.
    """

    def __init__(self, rowNum, colNum, connectN, targetScore, playerName1, playerName2) -> None:
        pass

    def __playBoard(self, curPlayer):
        """Handles the process of a player making a move on the board.

        Args:
            curPlayer (Player): The current player who is making the move.
        """
        pass

    def __changeTurn(self):
        """Switches the turn to the other player."""
        pass

    def playRound(self):
        """Plays a single round of the game."""
        pass

    def play(self):
        """Starts and manages the game play until a player wins."""
        pass

def main():
    """Main function to start the game."""
    game = Game(4, 4, 3, 2, 'P1', 'P2')
    game.play()

if __name__ == "__main__":
    main()
