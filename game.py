from player import Player
from enum import Enum
import bot


class AymanTicTacToe():
    """
    This class contains a main method playGame and helper methods that are required to 
    run a console-based Tic-Tac-Toe game.

    This class has been created and developed by Ayman Zuhair Shashavali.

    To run the game, an object of the class has to be made and the playGame method must be 
    called on the object.
    """

    def __init__(self) -> None:
        """
        This is the constructor method of the game that can be used to create an object of the
        game class.

        It initialises three class variables that are required to run the game.

        1. gameList :

        The gameList variable stores a list that is used to store the space, X or O 
        characters in the game.

        2. numberOfOccupiedPositions :

        This variable stores the number of positions in the gameList that are not available for
        any Player to add their character to.
        Essentially, it stores the number of characters in the list that are X or O.

        3. adjacentPositionsDict :

        This variable stores a dictionary with position indices as keys and a list of tuples as values.

        A tuple in the list of a particular position index contains two values that lie in a row/ column/ diagonal/ anti-diagonal
        of the game matrix. 

        For every position index in the game matrix, the dictionary contains a list of tuples that store all the indices near the position
        that are in adjacent rows, columns, diagonals anfd anti-diagonals.
        """

        self.gameList = [" "," "," "," "," "," "," "," "," "]
        self.numberOfOccupiedPositions = 0
        self.adjacentPositionsDict = {
                                        0: [(1, 2), (3, 6), (4, 8)],
                                        1: [(0, 2), (4, 7)],
                                        2: [(0, 1), (5, 8), (4, 6)],
                                        3: [(0, 6), (4, 5)],
                                        4: [(0, 8), (2, 6), (1, 7), (3, 5)],
                                        5: [(2, 8), (3, 4)],
                                        6: [(0, 3), (7, 8), (2, 4)],
                                        7: [(6, 8), (1, 4)],
                                        8: [(0, 4), (2, 5), (6, 7)]
                                    }

    def playGame(self):
        """
        This is the starting method that needs to be called to start the game by the game object.

        The game that I have created can be played by two players or by a single player against a bot.

        This method contains the logic of displaying the two modes of the game which the user can choose and 
        starts the chosen game mode by the user once the correct option is chosen.
        """

        print("\nWelcome to Ayman's Tic Tac Toe!")
        userOption = 0
        while (userOption != 3):
            print("\nPress 1 to play against a bot :")
            print("\nPress 2 to play against another Player :")
            print("\nPress 3 to exit the main menu :")
            userOption = int(input("\nEnter your option here: "))
            match userOption:
                case 1:
                    self.getPlayerAndBotDetails()
                    self.startGame()
                case 2:
                    self.getPlayersDetails()
                    self.startGame()
                case 3:
                    print("\nGood Bye! Have a nice day!")
                    break
                case _:
                    print("\nInvalid Option! Please Choose Another Option!")

    def getPlayerAndBotDetails(self):
        """
        This method takes the player and bots details from the user.
        """

        player1Name = input("\nEnter a name for the First Player: ")

        player1Character = None
        while (player1Character not in ["X", "O"]):

            player1Character = str(input("\nEnter the character for " + player1Name + " (X or O): ")).upper()
            self.player1 = Player(player1Character, player1Name)

            match player1Character:
                case "X":
                    self.player2 = self.getBotType("O")
                case "O":
                    self.player2 = self.getBotType("X")
                case _:
                    print("Invalid character! Please try entering X or O!")

    def getBotType(self, botCharacter : str) -> Player:
        """
        This method returns an Easy Bot or a Hard Bot based on the bot chosen by the user.
        """
        option = 0

        while option not in [1,2]:

            print("\nEnter 1 to play against an Easy Bot")
            print("\nEnter 2 to play against a Hard Bot")
            option = int(input("\nEnter your option here: "))

            match option:
                case 1:
                    return bot.EasyBot(botCharacter,self.gameList)
                case 2:
                    return bot.HardBot(botCharacter,self.gameList)
                case _:
                    print("\nInvalid option! Please try entering 1 or 2!")


    def getPlayersDetails(self):
        """
        This method takes the details of both the players of the game from the user.
        """

        player1Name = input("\nEnter a name for the First Player: ")
        player2Name = input("\nEnter a name for the Second Player: ")

        player1Character = None
        while (player1Character not in ["X", "O"]):

            player1Character = str(input("\nEnter the character for " + player1Name + " (X or O): ")).upper()
            self.player1 = Player(player1Character, player1Name)

            match player1Character:
                case "X":
                    self.player2 = Player("O", player2Name)
                case "O":
                    self.player2 = Player("X", player2Name)
                case _:
                    print("Invalid character! Please try entering X or O!")

    def resetGame(self):
        """
        This method resets the gameList to reference a new list with 9 empty positions marked by a space
        and resets the numberOfOccupiedPositions variable to 0.
        """
        self.gameList = [" "," "," "," "," "," "," "," "," "]
        self.numberOfOccupiedPositions = 0

    def startGame(self):
        """
        This method contains the main logic of the game in which the turns of the two players are handled.

        This method runs as long as there is no winner in the game or when there is no draw between the two players.
        """
        while True:

            self.playTurn(self.player1)

            player1GameStatus  = self.getGameStatus(self.player1)

            if player1GameStatus == GameStatus.DRAW :
                self.displayGameBoard()
                print("\nThe Game has resulted in a Draw between " + str(self.player1) + " and " + str(self.player2))
                break
            elif player1GameStatus == GameStatus.WIN :
                self.displayGameBoard()
                print("\n" + str(self.player1) + " has Won the game! ")
                break

            self.playTurn(self.player2)

            player2GameStatus  = self.getGameStatus(self.player2)
            
            if player2GameStatus == GameStatus.DRAW :
                self.displayGameBoard()
                print("\nThe Game has resulted in a Draw between " + str(self.player1) + " and " + str(self.player2))
                break
            elif player2GameStatus == GameStatus.WIN :
                self.displayGameBoard()
                print("\n" + str(self.player2) + " has Won the game! ")
                break
        
        self.resetGame()


    def playTurn(self, player : Player):
        """
        This method contains the logic of handling the turn of a player in the game.

        This logic includes displays the game matrix and available options to the player and letting the player choose 
        a correct position where the player wants to put their character at in the game matrix.

        """
        print("\n" + str(player) + "'s Turn: ")
        self.displayGameBoard()
        self.displayAvailablePositions()
        while self.getOptionValidity(player.getOption()) != True:
            print("\nInvalid Option, Please select a valid option!")
            print("\n" + str(player) + "'s Turn: ")
            self.displayGameBoard()
            self.displayAvailablePositions()

        chosenPosition = player.getLastChosenPosition() - 1
        playerCharacter = player.getCharacter()
        self.gameList[chosenPosition] = playerCharacter
        self.numberOfOccupiedPositions += 1
        
        print("\n" + str(player) + " has placed their character " + str(playerCharacter) + " at position: " + str(chosenPosition + 1) )


    def getOptionValidity(self, position : int) -> bool:
        """
        This method returns True if the given position is a valid position in the game matrix.
        """
        if 1 <= position <= 9:
            return self.gameList[position-1] == " "
        
        return False

    def displayAvailablePositions(self):
        """
        This method displays all the positions in the game matrix that are available for a player or bot to put their 
        character at.

        It displays information about the positions such as the row and the column a position it is located at for
        the player to understand the position they will be choosing.
        """
        for i in range(9):
            if self.gameList[i] == " ":
                columnNumber = (i % 3) + 1
                rowNumber = (i // 3) + 1
                printString = "Enter " + str(i + 1) + " to tick the position at Row: " + str(rowNumber) + " Column: " + str(columnNumber)
                print(printString)

    def getGameStatus(self, player : Player):
        """
        This method returns the status of the game. 
        That is, if the given player has won the game or if there is a draw.

        A player wins the game when their character occurs three consecutive times in the game.

        Generally, to check if the player has won the game, we would have to check all the rows,
        all the columns, the main diagonal and the anti diagonal.

        This would involve checking the 3 rows, 3 columns, 1 main diagonal, 1 anti diagonal of the game matrix 
        and for every check, we would have to check three positions by accessing the game array/list .

        So the overall number of times we check, that is, access the game matrix would be 24 times per method call.

        However, we can reduce the number of times we check the game matrix to atmost 8 times while checking for a win.

        This is possible by checking only the row, column, main diagonal and anti diagonal that contains the position
        chosen by the player to put the character at.

        For example, in the game below, the player with character X adds their character at position index 6

        
        | 0 O | 1   | 2 X |
        
        | 3 O | 4 X | 5   |
        
        | 6 * | 7   | 8   |
        
        To check for a win, we only need to check the remanining two characters in the last row, first column and the anti diagonal
        also store the character X.

        If we get a result where remaining two characters are also the same as the player's character, the player wins and the 
        game is over.
        
        Here, using the adjacentPositionsDict, we can get the list of tuples for position 6 which stores a tuple that contains 
        the other two position indices that are part of a row/ column/ main diagonal/ anti diagonal which contains position 6.

        The maximum number of times we need to check the game matrix or array is when the chosen position index is 4 
        as position index 4 lies on a row, column, the main diagonal and anti diagonal. 

        Hence, we would have to do 8 checks to check for a win for a character placed at 4.

        By using this trick, we can save considerable processing power and make the game faster.
        """
        lastOccupiedPosition = player.getLastChosenPosition()

        if lastOccupiedPosition != None :

            lastOccupiedPosition -= 1

            playerCharacter = player.getCharacter()

            adjacentPositions = self.adjacentPositionsDict.get(lastOccupiedPosition)

            for positionTuple in adjacentPositions:
                i, j = positionTuple
                if self.gameList[i] == self.gameList[j] == playerCharacter :
                    return GameStatus.WIN
            
        if self.numberOfOccupiedPositions == 9:
            return GameStatus.DRAW
            
        return GameStatus.IN_PROGRESS
    
    def displayGameBoard(self):
        """
        This method parses the gameList and outputs the game board to the console 
        that is understandable by the players of the game.
        """
        print("\n-------------")
        for i in range(0,3):
            characterRow = "|"
            for j in range(3):
                characterPosition = 3 * i + j
                characterRow += " " + self.gameList[characterPosition] + " |"
            print(characterRow)
            print("-------------")



class GameStatus(Enum):
    """
    This enumeration stores values that indicate the status of the game.

    I have used an enumeration because using number's would cause confusion amongst fellow 
    developers who are going through my code and enumerations make the code more understandable and maintainable.
    """

    WIN = 0
    DRAW = 1
    IN_PROGRESS = 2

if __name__ == "__main__":
    x = AymanTicTacToe()
    x.playGame()