from player import Player

class AymanTicTacToe():

    def __init__(self) -> None:
        self.gameList = ["  ","  ","  ","  ","  ","  ","  ","  ","  "] 

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
        while (player1Character not in ["X", "O"]):
            player1Character = str(input("Enter the character for Player 1 (X or O): ")).upper()
            match player1Character:
                case "X":
                    self.player1 = Player(player1Character)
                    self.player2 = Player("O")
                case "O":
                    self.player1 = Player(player1Character)
                    self.player2 = Player("X")
                case _:
                    print("Invalid character! Please try entering X or O!")

    
    def displayGameBoard(self):
        print("-------------")
        for i in range(0,3):
            characterRow = "|"
            for j in range(3):
                characterPosition = 3 * i + j
                characterRow += " " + self.gameList[characterPosition] + " |"
            print(characterRow)
            print("-------------")