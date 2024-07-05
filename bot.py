from player import Player
import random

"""
The Bot classes that I have created here are child classes of the Player class because:

1. Making both the Bots as seperate classes would have resulted in creation of unnecessary additional methods 
   that would cause code repetition and it would also decrease the maintainability of the game.

2. Considering that Bots can have their own character and potentially a name according to their difficulty, they can be considered as
   Players which depend on pre-coded instructions to play the game.

3. Even for Bots, we would have to keep track of the last chosen position to check for a win in the game which would have caused 
   code repetition of class attributes as well.

"""

class EasyBot(Player):
    """
    This class represents a Bot in the game that is easy to play against in the game.

    This class has been created and developed by Ayman Zuhair Shashavali
    """

    def __init__(self, playerCharacter: str, gameListReference: list) -> None:
        """
        This constructor is used to create an EasyBot object in the game.

        It has one class attribute stated below.

        1.gameListReference 

        This class attribute is used to store a reference to the game list/matrix of the game
        so that decisions can be taken by reading the game list.
        """
        super().__init__(playerCharacter, "Easy Bot")
        self.gameListReference = gameListReference

    def getOption(self) -> int:
        """
        This method returns an integer option that is available to place its character at in the game.

        The method iterates through the gameListReference to check for any available positions, that is, positions with spaces.
        Everytime a space is detected in a position index, the position index is added to the positionsList.

        Using randint function of random, I obtain a random integer index between 0 and the number of available positions - 1
        which is the maximum index value of positionsList.

        Using this index, I obtain the chosen position index stored at its place in the positionsList.

        And since the options start from 1 and ends at 9, I added 1 to the position index stored in the
        chosen position variable and this variable's value is returned.

        Using a while loop instead of this approach can cause delay in the game as it progresses.

        This is because we do not know after how many interations the randint function will return a correct position index
        and this can be slow down the game as it progresses because the number of available positions would decrease 
        and with that the probability of the randint function generating a correct position index value in an iteration would
        also decrease due to lesser number of correct options.

        In the last turn of the game, if the randint function has a lower probability to return a position index and at that position
        there is an empty space, the number of iterations to compute the correct value can go beyond 9, sometimes even 
        possibly reaching 10 times the value.

        Hence my first approach ensures that the number of iterations is constant for every method call, keeping the running time 
        of the game stable.

        """

        positionsList = []
        maxIndex = -1

        for position in range(len(self.gameListReference)):
            if self.gameListReference[position] == " ":
                positionsList.append(position)
                maxIndex += 1
                
        chosenIndex = random.randint(0, maxIndex)
        chosenPosition = positionsList[chosenIndex] + 1

        self.lastChosenPosition = chosenPosition

        return chosenPosition


class HardBot(Player):
    """
    This class represents a Bot in the game that is hard to play against in the game.

    This class has been created and developed by Ayman Zuhair Shashavali
    """

    def __init__(self, playerCharacter: str, gameListReference: list) -> None:
        """
        This constructor is used to create an HardBot object in the game.

        It has two class attribute stated below.

        1.gameListReference 

        This class attribute is used to store a reference to the game list/matrix of the game
        so that decisions can be taken by reading the game list.

        2.adjacentPositionsDict

        This variable stores a dictionary with position indices as keys and a list of tuples as values.

        A tuple in the list of a particular position index contains two values that lie in the row/ column/ diagonal/ anti-diagonal
        of the game matrix which contains the position index. 

        For every position index in the game matrix, the dictionary contains a list of tuples that store all the indices near the position
        that are in the adjacent row, column, diagonal and anti-diagonal.

        Using these two class attributes, we calculate the best option that can be returned.
        """
        super().__init__(playerCharacter, "Hard Bot")
        self.gameListReference = gameListReference
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

    def getOption(self) -> int:
        """
        This method returns an integer option that is available to place its character at in the game.

        This method returns a random position using the option selection logic of EasyBot
        if the last chosen position of the bot is None, that is, if it's the bot's first turn.
        If it's not the bot's first turn, the method checks for an optimal option using the last chosen position of the
        player in the following order :

        1. Using the adjacentPositionsDict, it checks the remaining two index positions of the 
           row/column/main-diagonal/anti-diagonal which contains the last chosen position.

           It checks if one index position is a space or available and if the other is occupied with the player's character
           and if any such row/column/main-diagonal/anti-diagonal is found, the available index position storing the space
           is returned.

        2. Then, the method checks if all the rows in the game have any two positions that are occupied with the 
           opponent's character and if the remaining position is available, that is, if it contains a space.
           If any such row is found, the index position that contains the space is returned.

        3. Then, the method checks if all the columns in the game have any two positions that are occupied with the 
           opponent's character and if the remaining position is available, that is, if it contains a space.
           If any such column is found, the index position that contains the space is returned.

        4. Then, the method checks if the main diagonal in the game has any two positions that are occupied with the 
           opponent's character and if the remaining position is available, that is, if it contains a space.
           If the above stated condition is true , the index position that contains the space is returned.

        5. Then, the method checks if the anti diagonal in the game has any two positions that are occupied with the 
           opponent's character and if the remaining position is available, that is, if it contains a space.
           If the above stated condition is true , the index position that contains the space is returned.

        6. Then, using the adjacentPositionsDict, again it checks the remaining two index positions of 
           the row/column/main-diagonal/anti-diagonal which contains the last chosen position.

           However this time, it checks if one index position is a space or available and if any such 
           row/column/main-diagonal/anti-diagonal is found, the available index position storing the space
           is returned.

        Here since the options start from 1 and ends at 9, 1 is added to the value being returned.
        """

        if self.lastChosenPosition != None :

            lastChosenPosition = self.lastChosenPosition

            lastChosenPosition -= 1

            adjacentPositions = self.adjacentPositionsDict.get(lastChosenPosition)

            #returns an empty position in a row/column/main-diagonal/anti-diagonal whose 
            #remaining positions are occupied by the player's character
            for positionTuple in adjacentPositions:
                i, j = positionTuple
                if (self.gameListReference[i] == self.playerCharacter and self.gameListReference[j] == " "):
                    self.lastChosenPosition = j + 1
                    return j + 1
                elif (self.gameListReference[j] == self.playerCharacter and self.gameListReference[i] == " "):
                    self.lastChosenPosition = i + 1
                    return i + 1
                
            opponentCharacter = self.getOpponentCharacter()
                
            # returns an empty position in a row whose two positions are occupied by the opponent character
            for i in range(3):

                if (self.gameListReference[i*3] == self.gameListReference[i*3 + 1] == opponentCharacter 
                    and self.gameListReference[i*3 + 2] == " ") :

                    self.lastChosenPosition = i*3 + 2 + 1
                    return i*3 + 2 + 1
                
                elif (self.gameListReference[i*3] == self.gameListReference[i*3 + 2] == opponentCharacter 
                    and self.gameListReference[i*3 + 1] == " ") :

                    self.lastChosenPosition = i*3 + 1 + 1
                    return i*3 + 1 + 1
                
                elif  (self.gameListReference[i*3 + 1] == self.gameListReference[i*3 + 2] == opponentCharacter 
                    and self.gameListReference[i*3] == " ") :

                    self.lastChosenPosition = i*3 + 1
                    return i*3 + 1
                
            # returns an empty position in a column whose two positions are occupied by the opponent character
            for i in range(3):

                if (self.gameListReference[0 + i] == self.gameListReference[3 + i] == opponentCharacter 
                    and self.gameListReference[6 + i] == " ") :

                    self.lastChosenPosition = 6 + i + 1
                    return 6 + i + 1
                
                elif (self.gameListReference[0 + i] == self.gameListReference[6 + i] == opponentCharacter 
                    and self.gameListReference[3 + i] == " ") :

                    self.lastChosenPosition = 3 + i + 1
                    return 3 + i + 1
                
                elif  (self.gameListReference[3 + i] == self.gameListReference[6 + i] == opponentCharacter 
                    and self.gameListReference[0 + i] == " ") :

                    self.lastChosenPosition = 0 + i + 1
                    return 0 + i + 1
                
            #returns an empty position in the main diagonal if two positions in it are occupied by the opponent character 
            if (self.gameListReference[0] == self.gameListReference[4] == opponentCharacter 
                    and self.gameListReference[8] == " ") :

                    self.lastChosenPosition = 8 + 1
                    return 8 + 1
                
            elif (self.gameListReference[0] == self.gameListReference[8] == opponentCharacter 
                and self.gameListReference[4] == " ") :

                self.lastChosenPosition = 4 + 1
                return 4 + 1
            
            elif  (self.gameListReference[4] == self.gameListReference[8] == opponentCharacter 
                and self.gameListReference[0] == " ") :

                self.lastChosenPosition = 0 + 1
                return 0 + 1
            
            #returns an empty position in the anti diagonal if two positions in it are occupied by the opponent character 
            if (self.gameListReference[2] == self.gameListReference[4] == opponentCharacter 
                    and self.gameListReference[6] == " ") :

                    self.lastChosenPosition = 6 + 1
                    return 6 + 1
                
            elif (self.gameListReference[2] == self.gameListReference[6] == opponentCharacter 
                and self.gameListReference[4] == " ") :

                self.lastChosenPosition = 4 + 1
                return 4 + 1
            
            elif  (self.gameListReference[4] == self.gameListReference[6] == opponentCharacter 
                and self.gameListReference[2] == " ") :

                self.lastChosenPosition = 2 + 1
                return 2 + 1
            

            #returns an empty position in a row/column/main-diagonal/anti-diagonal whose 
            #either one of the two positions are occupied the player's character.
            for positionTuple in adjacentPositions:
                    i, j = positionTuple
                    if (self.gameListReference[j] == " "):
                        self.lastChosenPosition = j + 1
                        return j + 1
                    elif (self.gameListReference[i] == " "):
                        self.lastChosenPosition = i + 1
                        return i + 1


        else :

            positionsList = []
            maxIndex = -1

            for position in range(len(self.gameListReference)):
                if self.gameListReference[position] == " ":
                    positionsList.append(position)
                    maxIndex += 1
 
            chosenIndex = random.randint(0, maxIndex)
            chosenPosition = positionsList[chosenIndex] + 1

            self.lastChosenPosition = chosenPosition

            return chosenPosition

    def getOpponentCharacter(self):
        if self.playerCharacter == "X":
            return "O"
        else:
            return "X"