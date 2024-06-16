from player import Player

class AymanTicTacToe():

    def __init__(self) -> None:
        self.gameList = ["  ","  ","  ","  ","  ","  ","  ","  ","  "] 

    def playGame():
        print("Welcome to Ayman's Tic Tac Toe!")
        while (userOption != 3):
            print("\nPress 1 to play against a bot :")
            print("\nPress 2 to play against another Player :")
            print("\nPress 3 to exit the main menu :")
            userOption = int(input())
            match userOption:
                case 1:
                    pass
                    break
                case 2:
                    pass
                    break
                case 3:
                    print("\nGood Bye! Have a nice day!")
                    break
                case _:
                    print("Invalid Option! Please Choose Another Option!")
                    break