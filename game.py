from player import Player
from enum import Enum


class AymanTicTacToe():

    def __init__(self) -> None:
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
        print("Welcome to Ayman's Tic Tac Toe!")
        userOption = 0
        while (userOption != 3):
            print("\nPress 1 to play against a bot :")
            print("\nPress 2 to play against another Player :")
            print("\nPress 3 to exit the main menu :")
            userOption = int(input())
            match userOption:
                case 1:
                    pass
                case 2:
                    self.startMultiplayerGame()
                case 3:
                    print("\nGood Bye! Have a nice day!")
                    break
                case _:
                    print("\nInvalid Option! Please Choose Another Option!")

    def startMultiplayerGame(self):
        player1Character = None
        while (player1Character not in ["X", "O"]):

            player1Character = str(input("Enter the character for Player 1 (X or O): ")).upper()
            self.player1 = Player(player1Character, "Player 1")

            match player1Character:
                case "X":
                    self.player2 = Player("O")
                case "O":
                    self.player2 = Player("X")
                case _:
                    print("Invalid character! Please try entering X or O!")

    def playTurn(self, player : Player):
        pass

    def displayAvailablePositions(self):
        for i in range(9):
            if self.gameList[i] == " ":
                columnNumber = (i % 3) + 1
                rowNumber = (i // 3) + 1
                printString = "Enter " + str(i + 1) + " to tick the position at Row: " + str(rowNumber) + " Column: " + str(columnNumber)
                print(printString)

    def getGameStatus(self, player : Player):
        if self.numberOfOccupiedPositions == 9:
            return GameStatus.DRAW
        
        lastOccupiedPosition = player.getLastChosenPosition()

        if lastOccupiedPosition != None :

            playerCharacter = player.getCharacter()

            adjacentPositions = self.adjacentPositionsDict.get(lastOccupiedPosition)

            for i, j in adjacentPositions:
                if self.gameList[i] == self.gameList[j] == playerCharacter :
                    return GameStatus.WIN
            
        return GameStatus.IN_PROGRESS
    
    def displayGameBoard(self):
        print("-------------")
        for i in range(0,3):
            characterRow = "|"
            for j in range(3):
                characterPosition = 3 * i + j
                characterRow += " " + self.gameList[characterPosition] + " |"
            print(characterRow)
            print("-------------")



class GameStatus(Enum):

    WIN = 0
    DRAW = 1
    IN_PROGRESS = 2