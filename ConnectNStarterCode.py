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
    EMPTY = 0  
    PLAYER1 = 1  
    PLAYER2 = 2  

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

    def __init__(self, playerName: str, playerNotation: Notation, curScore: int):
        self.__playerName = playerName
        self.__playerNotation = playerNotation
        self.__curScore = curScore

    def display(self) -> str:
        return f"Player: {self.__playerName}, Score: {self.__curScore}, Notation: {self.__playerNotation.name}"


    def addScoreByOne(self):
        """Increments the player's score by one."""
        self.__curScore += 1

    def getScore(self):
        """Returns the current score of the player."""
        return self.__curScore

    def getName(self):
        """Returns the name of the player."""
        return self.__playerName

    def getNotation(self):
        """Returns the notation used by the player."""
        return self.__playerNotation

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

    def __init__(self, rowNum: int, colNum: int):
        self.__rowNum = rowNum
        self.__colNum = colNum
        self.__grid = [[Notation.EMPTY for _ in range(colNum)] for _ in range(rowNum)]

    def initGrid(self):
        """Initializes the game board with empty cells."""
        self.__grid = [[Notation.EMPTY for _ in range(self.__colNum)] for _ in range(self.__rowNum)]

    def getColNum(self):
        """Returns the number of columns in the board."""
        return self.__colNum

    def placeMark(self, colNum: int, mark: Notation) -> bool:
        """Attempts to place a mark on the board at the specified column.

        Args:
            colNum (int): The column number where the mark is to be placed.
            mark (Notation): The mark to be placed on the board.

        Returns:
            bool: True if the mark was successfully placed, False otherwise.
        """
        if colNum < 0 or colNum >= self.__colNum or mark == Notation.EMPTY:
            print("Error: Invalid column number or marker")
            return False
        for row in reversed(self.__grid):
            if row[colNum] == Notation.EMPTY:
                row[colNum] = mark
                return True
        print("Column is full")
        return False

    def checkFull(self) -> bool:
        """Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != Notation.EMPTY for row in self.__grid for cell in row)

    def display(self):
        """Displays the current state of the board."""
        boardStr = "Current Board is:\n"
        for row in self.__grid:
            for cell in row:
                boardStr += 'O' if cell == Notation.EMPTY else ('R' if cell == Notation.PLAYER1 else 'Y')
            boardStr += '\n'
        print(boardStr)

    # Private methods for internal use
    def __checkWinHorizontal(self, target):
        for row in self.__grid:
            for col in range(self.__colNum - target + 1):
                if all(row[col + i] == row[col] != Notation.EMPTY for i in range(target)):
                    return row[col]
        return None

    def __checkWinVertical(self, target):
        for col in range(self.__colNum):
            for row in range(self.__rowNum - target + 1):
                if all(self.__grid[row + i][col] == self.__grid[row][col] != Notation.EMPTY for i in range(target)):
                    return self.__grid[row][col]
        return None

    def __checkWinOneDiag(self, target, rowNum, colNum):
        for row in range(self.__rowNum - target + 1):
            for col in range(self.__colNum - target + 1):
                if all(self.__grid[row + i][col + i] == self.__grid[row][col] != Notation.EMPTY for i in range(target)):
                    return self.__grid[row][col]
                if all(self.__grid[row + target - 1 - i][col + i] == self.__grid[row + target - 1][col] != Notation.EMPTY for i in range(target)):
                    return self.__grid[row + target - 1][col]
        return None

    def __checkWinAntiOneDiag(self, target, rowNum, colNum):
        for row in range(self.__rowNum - 1, target - 2, -1):
            for col in range(self.__colNum - target + 1):
                if all(self.__grid[row - i][col + i] == self.__grid[row][col] != Notation.EMPTY for i in range(target)):
                    return self.__grid[row][col]
                if all(self.__grid[row - target + 1 + i][col + i] == self.__grid[row - target + 1][col] != Notation.EMPTY for i in range(target)):
                    return self.__grid[row - target + 1][col]
        return None

    def __checkWinDiagonal(self, target):
        return self.__checkWinOneDiag(target, self.__rowNum, self.__colNum) or self.__checkWinAntiOneDiag(target, self.__rowNum, self.__colNum)

    def checkWin(self, target):
        """Checks if there is a winning condition on the board.

        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        return self.__checkWinHorizontal(target) or self.__checkWinVertical(target) or self.__checkWinDiagonal(target)

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
        self.__board = Board(rowNum, colNum)  # Initialize the game board
        self.__connectN = connectN  # Number of consecutive marks needed for a win
        self.__targetScore = targetScore  # Score needed to win the game
        # Initialize the players
        self.__playerList = [Player(playerName1, Notation.PLAYER1, 0), Player(playerName2, Notation.PLAYER2, 0)]
        self.__curPlayer = self.__playerList[0]

    def __playBoard(self, curPlayer):
        """Handles the process of a player making a move on the board.

        Args:
            curPlayer (Player): The current player who is making the move.
        """
        isPlaced = False
        while not isPlaced:
            try:
                colNum = int(input(f"{curPlayer.getName()}, enter column number to place your mark: "))
                if colNum < 0 or colNum >= self.__board.getColNum():
                    raise ValueError
                isPlaced = self.__board.placeMark(colNum, curPlayer.getNotation())
            except ValueError:
                print("Invalid input. Please enter a valid column number.")

    def __changeTurn(self):
        """Switches the turn to the other player."""
        self.__curPlayer = self.__playerList[1] if self.__curPlayer == self.__playerList[0] else self.__playerList[0]

    def playRound(self):
        """Plays a single round of the game."""
        curWinnerNotation = None
        self.__board.initGrid()
        self.__curPlayer = self.__playerList[0]
        print("Starting a new round")

        while not curWinnerNotation and not self.__board.checkFull():
            self.__curPlayer.display()
            self.__board.display()
            self.__playBoard(self.__curPlayer)
            curWinnerNotation = self.__board.checkWin(self.__connectN)
            if curWinnerNotation:
                print(f"Winner: {self.__curPlayer.getName()}")
                self.__board.display()
                self.__curPlayer.addScoreByOne()
                break
            elif self.__board.checkFull():
                print("Board is full. No winner for this round.")
                break
            self.__changeTurn()

    def play(self):
        """Starts and manages the game play until a player wins."""
        while all(player.getScore() < self.__targetScore for player in self.__playerList):
            self.playRound()

        print("Game Over")
        for player in self.__playerList:
            print(player.display())

def main():
    """Main function to start the game."""
    game = Game(4, 4, 3, 2, 'P1', 'P2')
    game.play()

if __name__ == "__main__":
    main()
