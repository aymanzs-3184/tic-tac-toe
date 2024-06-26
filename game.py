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
        print("\nWelcome to Ayman's Tic Tac Toe!")
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

    def resetGame(self):
        self.gameList = [" "," "," "," "," "," "," "," "," "]
        self.numberOfOccupiedPositions = 0

    def startMultiplayerGame(self):
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

        while self.numberOfOccupiedPositions < 9:

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
        if 1 <= position <= 9:
            return self.gameList[position-1] == " "
        
        return False

    def displayAvailablePositions(self):
        for i in range(9):
            if self.gameList[i] == " ":
                columnNumber = (i % 3) + 1
                rowNumber = (i // 3) + 1
                printString = "Enter " + str(i + 1) + " to tick the position at Row: " + str(rowNumber) + " Column: " + str(columnNumber)
                print(printString)

    def getGameStatus(self, player : Player):
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
        print("\n-------------")
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

x = AymanTicTacToe()
x.playGame()